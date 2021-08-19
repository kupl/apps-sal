class Solution:

    def soupServings(self, N: int) -> float:
        if N > 5000:
            return 1

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return (dp(a - 100, b) + dp(a - 75, b - 25) + dp(a - 50, b - 50) + dp(a - 25, b - 75)) / 4
        return dp(N, N)
