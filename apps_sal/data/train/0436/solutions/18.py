class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dp(m):
            if m == 0: return 0
            if m == 1: return 1
            return min(
                m % 2 + 1 + dp(m // 2),
                m % 3 + 1 + dp(m // 3)
            )
        return dp(n)
