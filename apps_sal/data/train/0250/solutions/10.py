import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        # consider with min coefficient
        workers = sorted([[w/q,q,w] for q,w in zip(quality, wage)])
        res = float('inf')
        pool = []
        sumq = 0
        for r, q, w in workers:
            # candidates with maximaml quality first
            heappush(pool, -q)
            sumq += q
            if len(pool) > K:
                # remove redundant
                a = heappop(pool)
                sumq += a # subtract a from sum
            if len(pool) == K:
                res = min(res, r * sumq)
        return res        
                
                
                
                
            
            

                           
            

