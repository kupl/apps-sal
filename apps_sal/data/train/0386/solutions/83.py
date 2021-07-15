class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n + 1)]
        for i in range(5):
            dp[n][i] = 1
        
        mod = 10**9 + 7
        for i in range(n - 1, 0, -1):
            for j in range(5):
                if j == 0:
                    dp[i][j] = dp[i + 1][j + 1]
                elif j == 1:
                    dp[i][j] = (dp[i + 1][j - 1] + dp[i + 1][j + 1])%mod
                elif j == 2:
                    dp[i][j] = (dp[i + 1][j - 1] + dp[i + 1][j + 1])%mod
                    dp[i][j] = (dp[i][j] + dp[i + 1][j - 2] + dp[i + 1][j + 2])%mod
                elif j == 3:
                    dp[i][j] = (dp[i + 1][j - 1] + dp[i + 1][j + 1])%mod
                elif j == 4:
                    dp[i][j] = dp[i + 1][0]
        
        # print(dp)
        res = 0
        for j in range(5):
            res = (res + dp[1][j])%mod
        return res
