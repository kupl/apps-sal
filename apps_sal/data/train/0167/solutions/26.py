class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('Inf')] * (N + 1) for _ in range(K + 1)]

        for i in range(1, K + 1):
            dp[i][0], dp[i][1] = 0, 1

        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[i][j - k] > dp[i - 1][k - 1]:
                    k += 1
                dp[i][j] = 1 + dp[i - 1][k - 1]

        return dp[K][N]
