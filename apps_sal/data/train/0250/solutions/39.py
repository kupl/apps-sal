class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        x = sorted((wage/quality, wage, quality) for wage, quality in zip(wage, quality))        
        cur_sum = 0
        heap = []
        res = sys.maxsize
        for r, w, q in x:
            heapq.heappush(heap, -q)
            cur_sum+=q
            if len(heap) > K:
                cur_sum += heapq.heappop(heap)            
            if len(heap) == K:
                res = min(res, cur_sum*r)
        
        return res    
