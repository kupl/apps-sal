class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target or d > target:
            return 0
    
        if d == 1 and f >= target:
            return 1
        
        rows = d+1
        cols = target+1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
            
        for i in range(1,min(f+1, cols)):
            dp[1][i] = 1

            
        for i in range(2, rows):
            for j in range(i, cols):
                
                start = max(1, j - f)
                dp[i][j] = sum(dp[i-1][start:j]) % 1000000007
                
                
        return dp[d][target]
                

