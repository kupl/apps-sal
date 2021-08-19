from collections import deque


class Solution:

    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        m = [{} for i in range(n)]
        for (edge, d) in zip(edges, succProb):
            (s, e) = edge
            m[s][e] = m[e][s] = d
        res = [0] * n
        res[start] = 1
        q = [[-1, start]]
        while q and res[end] == 0:
            tmp = heapq.heappop(q)
            (prob, cur) = (-tmp[0], tmp[1])
            res[cur] = prob
            for (nxt, np) in m[cur].items():
                if res[nxt] != 0:
                    continue
                heapq.heappush(q, [-np * prob, nxt])
        return res[end]
