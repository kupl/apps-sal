class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        '\n        {0: [(0.5, 1), (0.2, 2)], 1: [(0.5, 0), (0.5, 2)], 2: [(0.5, 1), (0.2, 0)]}\n        '
        for (edge, prob) in zip(edges, succProb):
            (x, y) = edge
            g[x].append((prob, y))
            g[y].append((prob, x))
        print(g)
        (q, vis) = ([(-1, start)], set())
        cand = []
        while q:
            (prob, node) = heapq.heappop(q)
            if node == end:
                cand.append(-prob)
            if node not in vis:
                vis.add(node)
                for (next_prob, nbrs) in g[node]:
                    if nbrs not in vis:
                        heapq.heappush(q, (prob * next_prob, nbrs))
        print(cand)
        return max(cand, default=0)
