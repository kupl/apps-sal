class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(d, t):
            print((d,t))
            if d == 0:
                return 1 if t == 0 else 0
            return sum(dp(d-1, t - x) for x in range(1, f+1))
        return dp(d, target)%(10**9 + 7)
        

