class Solution:                
    
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:        
        import heapq
        heap = []
        hm = {}
        for i in nums:
            if i not in hm:
                hm[i] = 0
            hm[i] += 1
            
        for i in hm:
            heapq.heappush(heap, (i, hm[i]))
            
        while len(heap):
            pending = []
            x = heapq.heappop(heap)
            if x[1] - 1 > 0:
                pending.append((x[0], x[1] - 1))
            
            cnt = 1
            last = x[0]
            while cnt < k:
                if len(heap) == 0 or heap[0][0] != last + 1:
                    return False
                n = heapq.heappop(heap)
                if n[1] - 1 > 0:
                    pending.append((n[0], n[1]-1))
                last = n[0]
                cnt += 1
            for x in pending:
                heapq.heappush(heap, x)
        return True
        
                
        
                
            
            
                
            
        
        
        
        
        
        
                
                
        
    

