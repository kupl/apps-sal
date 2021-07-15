class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if not arrLen or not steps:return 1
        if arrLen == 1: return 1 #stay all the time 
        
        shorter = min(steps, arrLen)
        dp = [[0 for _ in range(shorter)] for _ in range(steps+1)]
        dp[0][0] = 1
        dp[1][0] = 1
        
        for i in range(1, steps+1):
            for j in range(shorter):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
                elif j == shorter - 1:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1]
        return dp[-1][0] % (10**9 + 7)
    
        
                    

