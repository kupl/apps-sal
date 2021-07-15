class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0]*(N+1) for _ in range(K+1)]
        for i in range(1, N+1):
            dp[1][i] = i
        for i in range(2, K+1):
            s = 1
            for j in range(1, N+1):
                dp[i][j] = j
                while s<j and dp[i][j-s]>dp[i-1][s-1]:
                    s += 1
                dp[i][j] = min(dp[i][j], max(dp[i][j-s], dp[i-1][s-1])+1)


        return dp[K][N]

