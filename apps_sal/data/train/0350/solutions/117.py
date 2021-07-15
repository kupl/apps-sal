from collections import Counter

def solve(A, K):
    count = Counter()
    front = iter(A)
    
    ans = 0
    size = 0
    for k in A:
        count[k] += 1
        size += 1
        
        while len(count) > K:
            key = next(front)
            count[key] -= 1
            size -= 1
            if count[key] == 0:
                del count[key]

        ans += size
    
    return ans
            
            
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        cx = Counter()
        cy = Counter()
        
        fx = iter(A)
        fy = iter(A)
        
        sx = 0
        sy = 0
        
        ans = 0
        for k in A:
            cx[k] += 1
            cy[k] += 1
            sx += 1
            sy+= 1
            
            while len(cx) > K:
                key = next(fx)
                cx[key] -= 1
                sx -= 1
                if cx[key] == 0:
                    del cx[key]
                    
            while len(cy) > K - 1:
                key = next(fy)
                cy[key] -= 1
                sy -= 1
                if cy[key] == 0:
                    del cy[key]
                    
            ans += sx - sy
            
        return ans
                
            
                
                
                
                
                
                

