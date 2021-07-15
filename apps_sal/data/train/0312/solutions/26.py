class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        s = [0]
        
        for x in A: 
            s += s[-1] +x, 
      
        q = []
        res = len(A) + 2
        
        for i, val in enumerate(s): 
            
            while q and val - q[0][0] >= K:
                res = min(res, i - heapq.heappop(q)[1]) 
            
            heapq.heappush(q, (val, i))
            
        return res if res < len(A) + 2 else -1 

            
        

