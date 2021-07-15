class Solution:
    def f(self, pivot: int, eggs: int, floors: int) -> int:
        
        ans, r = 0, 1        
        
        for idx in range(1, eggs+1):
            r *= (pivot - idx+1)
            r //= idx
            ans += r
            
            if ans >= floors:
                break
        
        return ans
    
    def superEggDrop(self, eggs: int, floors: int) -> int:
        
        lo, hi = 1, floors
        
        while lo < hi:
            
            mi = (lo + hi) // 2
            
            if self.f(mi, eggs, floors) < floors:
                lo = mi + 1
            else:
                hi = mi
        
        return lo
