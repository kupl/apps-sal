import collections
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        p = [0]
        
        for x in A:
            p.append(p[-1] + x)
            
        # print(p)
        
        ans = n+1
        q = collections.deque()
        
        for key,val in enumerate(p):
            while q and val <= p[q[-1]]:
                q.pop()
            
            while q and val - p[q[0]] >= K:
                ans = min(ans, key - q.popleft())
                
            q.append(key)
            # print(q)
            
        return ans if ans < n+1 else -1
        
        
        
            
                
            

