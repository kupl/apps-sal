class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target or d > target:
            return 0
        
        if d == 1:
            if target <=f:
                return 1
            else:
                return 0
        
        M = 10**9 + 7
        
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        
        dp[0][0] = 1
        
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                
                if j == 1:
                    dp[i][j] = dp[i - 1][0] 
                elif j <= f:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]                
                else:
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] - dp[i - 1][j -f - 1])
                    
        return dp[d][target] % M
