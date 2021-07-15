from functools import lru_cache
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def dfs(s, l):
            if s == steps:
                if l == 0:
                    return 1
                return 0
            
            return (dfs(s + 1, l) + (dfs(s + 1, l + 1) if l < arrLen-1 else 0 )+ (dfs(s + 1, l - 1) if l else 0)) % mod
        return dfs(0, 0)
