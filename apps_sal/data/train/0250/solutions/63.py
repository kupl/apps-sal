from heapq import heappush, heappop

from fractions import Fraction

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [(Fraction(w,q), q, w) for w, q in zip(wage, quality)]
        workers.sort()
        
        best = float('inf')
        queue = []
        sumq = 0
        
        for ratio, q, w in workers:
            heappush(queue, -q)
            sumq += q
            
            if len(queue) > K:
                sumq += heappop(queue)
            
            if len(queue) == K:
                best = min(best,ratio * sumq)

        return best

