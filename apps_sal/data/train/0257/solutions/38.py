class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        G = defaultdict(list)
        P = {}
        for (i, j), p in zip(edges, succProb):
            G[i].append(j)
            G[j].append(i)
            P[i, j] = P[j, i] = p
        hp = [(-1, start)]
        seen = {start: 1}
        while hp:
            prob, node = heapq.heappop(hp)
            prob *= -1
            if node == end:
                return prob
            for nei in G[node]:
                tmp = seen[node] * P[node, nei]
                if nei not in seen or seen[nei] < tmp:
                    heapq.heappush(hp, (-tmp, nei))
                    seen[nei] = tmp
        return 0
                    

