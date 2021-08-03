import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adj = {i: [] for i in range(n)}
        best = [0] * n

        for edge, prob in zip(edges, succProb):
            u, v = edge
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        queue = []
        heapq.heappush(queue, (-1, start))
        best[start] = 1
        while queue:
            prob, v = heapq.heappop(queue)
            prob = - prob
            if v == end:
                return prob
            if prob < best[v]:
                continue
            for nxt, np in adj[v]:
                if nxt != v:
                    tmp = np * prob
                    if tmp > best[nxt]:
                        best[nxt] = tmp
                        heapq.heappush(queue, (-tmp, nxt))

        return 0
