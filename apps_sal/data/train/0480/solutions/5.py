class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n=min(arrLen,steps)
        m= (10**9) + 7
        dp=[[0 for i in range(n)] for i in range(steps+1)]
        dp[0][0]=1
        for i in range(1,steps+1):
            for j in range(n):
                if(j-1<0):
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j+1] ) % m
                elif(j+1>=n):
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j-1])%m
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j-1]+dp[i-1][j+1]) % m
        return dp[steps][0]
                    

