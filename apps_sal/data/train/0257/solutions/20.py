class Solution:

    def maxProbability(self, n, edges, succProb, start, end) -> float:
        g = [[] for _ in range(n)]
        prob = [0.0 for _ in range(n)]
        prob[start] = 1.0
        for ((a, b), p) in zip(edges, succProb):
            g[a].append((p, b))
            g[b].append((p, a))
        pq = [(-1.0, start)]
        while pq:
            (p, v) = heapq.heappop(pq)
            if prob[v] + p:
                continue
            if v == end:
                return prob[v]
            for (ep, n) in g[v]:
                _p = ep * prob[v]
                if _p > prob[n]:
                    prob[n] = _p
                    heapq.heappush(pq, (-_p, n))
        return 0
