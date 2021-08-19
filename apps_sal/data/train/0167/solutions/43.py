class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        for n in range(1, N + 1):
            dp[1][n] = n
        for k in range(2, K + 1):
            dp[k][1] = 1
        for k in range(2, K + 1):
            m = 1
            for n in range(2, N + 1):
                while m < n and dp[k - 1][m - 1] < dp[k][n - m]:
                    m += 1
                dp[k][n] = max(dp[k - 1][m - 1], dp[k][n - m]) + 1
        return dp[-1][-1]
