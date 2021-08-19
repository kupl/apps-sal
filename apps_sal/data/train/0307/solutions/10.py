class Solution:

    def soupServings(self, N: int) -> float:
        memo = {}
        if N > 4800:
            return 1

        def dp(a, b):
            if (a, b) in memo:
                return memo[a, b]
            if a <= 0 and b > 0:
                return 1
            if a <= 0 and b <= 0:
                return 0.5
            if a > 0 and b <= 0:
                return 0
            memo[a, b] = (dp(a - 100, b) + dp(a - 75, b - 25) + dp(a - 50, b - 50) + dp(a - 25, b - 75)) / 4
            return memo[a, b]
        return dp(N, N)
