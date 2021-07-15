class Solution:
    def superEggDrop(self, e: int, f: int) -> int:
        
        self.cache = [[-1]*(f+1) for _ in range(e+1)]
        
        return self.drop(e,f)
    
    def drop(self,e,f):
        
        if f == 0 or f == 1:
            return f
        
        if e == 1:
            return f
        
        if self.cache[e][f] != -1:
            return self.cache[e][f]
        
        ans = float('inf')
        
        l = 1
        h = f
        
        while l <= h:
            
            mid = (l+h)//2
            
            low = 0
            high = 0
            
            if self.cache[e-1][mid-1] != -1:
                low = self.cache[e-1][mid-1]
            else:
                low = self.drop(e-1,mid-1)
            
            if self.cache[e][f-mid] != -1:
                high = self.cache[e][f-mid]
            else:
                high = self.drop(e,f-mid)
            
            if low < high:
                
                l = mid + 1
                
            else:
                
                h = mid -1
            ans = min(max(low,high)+1,ans)
            
        
#         for k in range(1,f+1):
            
#             low = 0
#             high = 0
            
#             if self.cache[e-1][k-1] != -1:
#                 low = self.cache[e-1][k-1]
#             else:
#                 low = self.drop(e-1,k-1)
            
#             if self.cache[e][f-k] != -1:
#                 high = self.cache[e][f-k]
#             else:
#                 high = self.drop(e,f-k)
            
#             ans = min(max(low,high)+1,ans)
            
        self.cache[e][f] = ans
            
        return ans

