class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))
        #print(workers)
        min_val = float('Inf')
        #print(min_val)
        
        pool = []
        sum_q = 0
        for r, q, w in workers:
            heapq.heappush(pool, -q)
            sum_q += q
            if len(pool) > K:
                sum_q += heapq.heappop(pool)
            if len(pool) == K:
                min_val = min(min_val, r * sum_q)
        return min_val

