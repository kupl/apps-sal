class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        dp[1] = list(range(N + 1))
        for i in range(2, K + 1):
            k = 1
            for j in range(1, N + 1):
                while k < j + 1 and dp[i][j - k] > dp[i - 1][k - 1]:
                    k += 1
                dp[i][j] = 1 + dp[i - 1][k - 1]
        return dp[-1][-1]
