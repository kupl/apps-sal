import math


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [0 for _ in range(n + 1)]

        dp[1] = 1

        for i in range(2, n + 1):
            N = (i - 1) * 2 + 1
            dp[i] = (N + math.factorial(N) // (math.factorial(N - 2) * 2)) * dp[i - 1] % MOD

        return dp[n]
