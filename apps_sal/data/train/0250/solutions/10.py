import heapq


class Solution:

    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        workers = sorted([[w / q, q, w] for (q, w) in zip(quality, wage)])
        res = float('inf')
        pool = []
        sumq = 0
        for (r, q, w) in workers:
            heappush(pool, -q)
            sumq += q
            if len(pool) > K:
                a = heappop(pool)
                sumq += a
            if len(pool) == K:
                res = min(res, r * sumq)
        return res
