class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        dq = deque([(0,0)])
        res = float('inf')
        p = 0
        for i, a in enumerate(A):
            p += a
            while dq and p<=dq[-1][0]:
                dq.pop()
                
            while dq and p-dq[0][0]>=K:
                res = min(res, i+1-dq.popleft()[1])
                
            dq.append((p, i+1))
            
        return res if res!=float('inf') else -1
        
                
                

