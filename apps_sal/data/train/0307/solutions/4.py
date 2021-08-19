class Solution:

    def soupServings(self, N: int) -> float:
        (q, r) = divmod(N, 25)
        N = q + (r > 0)
        if N >= 500:
            return 1
        memo = {}

        def dp(x, y):
            if (x, y) not in memo:
                if x <= 0 or y <= 0:
                    res = 0.5 if x <= 0 and y <= 0 else 1.0 if x <= 0 else 0.0
                else:
                    res = 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2, y - 2) + dp(x - 1, y - 3))
                memo[x, y] = res
            return memo[x, y]
        return dp(N, N)
