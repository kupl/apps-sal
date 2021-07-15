class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        ### dp[steps][pos]
        modulo = 10 ** 9 + 7
        
        maxPos = min(steps + 1, arrLen)
        
        dp = [ [0 for _ in range(maxPos+1)] for _ in range(steps + 1) ]
        
        dp[1][0], dp[1][1] = 1, 1
        
        ### dp[s][p] = dp[s-1][p] + dp[s-1][p-1] + dp[s-1][p+1]
        
        for i in range(2, steps+1):
            for j in range(maxPos):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % modulo
                    
                if j - 1 >= 0:
                    dp[i][j] += dp[i-1][j-1] % modulo
        
        return dp[steps][0]
