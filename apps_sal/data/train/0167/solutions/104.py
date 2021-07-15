class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[None] * K for _ in range(N+1)]
        for j in range(K):
            dp[0][j] = 0
        for i in range(1, N+1):
            dp[i][0] = i
        for j in range(1, K):
            dp[1][j] = 1
            m = 1
            for i in range(2, N+1):
                while m < i and dp[i-m][j] >= dp[m-1][j-1] and dp[i-m-1][j] >= dp[m][j-1]:
                    m += 1
                dp[i][j] = max(dp[i-m][j], dp[m-1][j-1]) + 1
                # for m in range(1, i+1):
                #     dp[i][j] = min(dp[i][j], max(dp[m-1][j-1], dp[i-m][j]) + 1)
        return dp[N][K-1]
