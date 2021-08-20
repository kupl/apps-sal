class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = max(dp[m][k], dp[m - 1][k] + 1 + dp[m - 1][k - 1])
            if dp[m][k] >= N:
                return m
