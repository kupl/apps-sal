import math
class Solution:
    def soupServings(self, N: int) -> float:
        
        
        N = math.ceil(N/25)
        
        if N>=1000:
            return 1
        
        dp = [[1 for i in range(N+1)] for j in range(N+1)]
        
        for i in range(0,N+1):
            dp[i][0] = 0
            
        dp[0][0] = 0.5    
            
        for i in range(1,N+1):
            for j in range(1,N+1):
                M = lambda x: max(0,x)   
                dp[i][j] = 0.25 * (dp[M(i - 4)][j] + dp[M(i -3)][j - 1] 
                               + dp[M(i - 2)][M(j - 2)] + dp[i - 1][M(j - 3)])   
                
                if(1 - dp[i][j] < 0.000001):
                    break
        
            if(1 - dp[i][i] < 0.000001):
                break

        return dp[N][N]                
                    

