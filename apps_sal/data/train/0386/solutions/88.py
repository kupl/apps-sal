class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 10**9+7
        dp = [[0 for j in range(n+1)] for i in range(5)]
        for i in range(5):
            dp[i][1] = 1
            
#         for i in range(5):
#             print(dp[i])
        
        for j in range(2, n+1):
            dp[0][j] = dp[1][j-1]+dp[2][j-1]+dp[4][j-1]
            dp[1][j] = dp[0][j-1]+dp[2][j-1]
            dp[2][j] = dp[1][j-1]+dp[3][j-1]
            dp[3][j] = dp[2][j-1]
            dp[4][j] = dp[2][j-1]+dp[3][j-1]
        
        res = 0
        for i in range(5):
            res += dp[i][n]
        return res%M
