class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        @lru_cache(None)
        def dp(k, n):
            if n == 0: return 0
            if k == 1: return n
            
            res = float('inf')
            
            lo = 1
            hi = n
            
            while lo <= hi:
                mid = (lo + hi) // 2
                
                broken = dp(k - 1, mid - 1)
                no_broken = dp(k, n - mid)
                
                if broken > no_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, no_broken + 1)
            return res
        
        return dp(K, N)
