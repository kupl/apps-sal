class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for i in range(K + 1)] for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = 1 + dp[m - 1][k - 1] + dp[m - 1][k]
            if dp[m][k] >= N:
                return m
