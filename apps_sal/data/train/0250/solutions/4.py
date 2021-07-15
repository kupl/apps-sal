class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))
        print(workers)

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            #print(pool)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)
                #print(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)
                #print(sumq)
                #print(pool)

        return float(ans)
