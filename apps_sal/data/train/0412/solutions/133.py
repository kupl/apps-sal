class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        z = 10**9+7
        def sol(n,m,t):
            
            dp=[[0 for i in range(t+1)] for j in range(n+1)]
            
            for i in range(1,min(t+1,m+1)):
                dp[1][i]=1
            
            for i in range(1,n+1):
                for j in range(1,t+1):
                    for k in range(1,min(j,m+1)):
                           dp[i][j]+=(dp[i-1][j-k])% z
                    
            return dp[n][t]%z
                          
        return sol(d,f,target)%z
                          

