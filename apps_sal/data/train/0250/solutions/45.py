class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratios = [(wi/qi, qi) for wi, qi in zip(wage, quality)]
        ratios.sort()
        
        res = float('inf')
        pq = []
        cur = 0
        
        for i, (ratio, q) in enumerate(ratios):
            if i >= K - 1:
                res = min(res, ratio*(q + cur))
                
            cur += q
            heapq.heappush(pq, -q)
            
            if len(pq) > K - 1:
                cur += heapq.heappop(pq)
        return res
                

