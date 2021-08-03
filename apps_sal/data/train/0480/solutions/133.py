class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dp(index, steps):
            if index < 0 or index >= arrLen:
                return 0
            if steps == 0:
                if index == 0:
                    return 1
                return 0
            return (dp(index - 1, steps - 1) + dp(index + 1, steps - 1) + dp(index, steps - 1)) % mod

        return dp(0, steps) % mod
