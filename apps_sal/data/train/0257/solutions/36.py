class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = collections.defaultdict(list)
        for ((u, v), p) in zip(edges, succProb):
            g[u].append((v, p))
            g[v].append((u, p))
        q = [(-1, start)]
        seen = set()
        while q:
            (p, u) = heapq.heappop(q)
            if u in seen:
                continue
            seen.add(u)
            if u == end:
                return -p
            for (v, pp) in g[u]:
                if v not in seen:
                    heapq.heappush(q, (p * pp, v))
        return 0
