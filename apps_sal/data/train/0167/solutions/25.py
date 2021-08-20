class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[i for i in range(N + 1)]]
        for _ in range(K - 1):
            dp.append([0, 1] + [0] * (N - 1))
        for i in range(1, K):
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[i][j - k] > dp[i - 1][k - 1]:
                    k += 1
                dp[i][j] = 1 + dp[i - 1][k - 1]
        return dp[-1][-1]
