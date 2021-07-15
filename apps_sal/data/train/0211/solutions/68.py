class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        from functools import lru_cache
        
        L = len(s)
        
        @lru_cache(None)
        def DP(idx, seen):
            if idx == L:
                return len(seen)
            res = 0
            for i in range(idx+1, L+1):
                temp = s[idx:i]
                if temp in seen:
                    continue
                res = max(res, DP(i, seen|{temp}))
            return res
                
            
        
        return DP(0, frozenset())
                    
        

