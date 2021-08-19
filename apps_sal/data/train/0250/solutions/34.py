import heapq


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted(((w / q, w, q) for (w, q) in zip(wage, quality)))
        ans = float('inf')
        pool = []
        sum_q = 0
        for (ratio, w, q) in workers:
            heapq.heappush(pool, -q)
            sum_q += q
            if len(pool) > K:
                sum_q += heapq.heappop(pool)
            if len(pool) == K:
                ans = min(ans, ratio * sum_q)
        return float(ans)
