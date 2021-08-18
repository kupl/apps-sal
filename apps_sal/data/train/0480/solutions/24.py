class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def dp(index, steps):
            if index < 0 or index == arrLen:
                return 0

            if steps == 0:
                return 1 if index == 0 else 0

            ans = 0
            for i in range(-1, 2, 1):
                ans += dp(index + i, steps - 1)
                ans %= (10**9 + 7)
            return ans

        return dp(0, steps)
