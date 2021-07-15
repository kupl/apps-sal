class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for i in range(d+1)]
        for i in range(1,d+1):
            for j in range(1,target+1):
                if i ==1:
                    if j<=f:
                        dp[i][j]=1
                else:
                    if j>=i:
                        for k in range(1,min(j+1,f+1)):
                            dp[i][j] += dp[i-1][j-k]
        
        return (dp[-1][-1]%((10**9)+7))
