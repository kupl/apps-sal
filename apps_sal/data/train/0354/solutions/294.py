class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7
        dp = [[0 for _ in range(7)] for _ in range(n)]
        for i in range(6):
            dp[0][i] = 1
            
        dp[0][6] = 6
        for i in range(1, n):
            sumi = 0
            for j in range(6):
                diff = i - rollMax[j]
                if(diff<0):
                    dp[i][j] = dp[i - 1][6]
                    sumi = (sumi + dp[i][j])%mod
                else:
                    if(diff>=1):
                        remove = (dp[diff-1][6] - dp[diff-1][j] + mod)%mod
                        dp[i][j] = (dp[i - 1][6] - remove + mod)%mod
                    else:
                        dp[i][j] = (dp[i - 1][6] - 1)%mod
                    
                    sumi = (sumi + dp[i][j])%mod
            dp[i][6] = sumi
        
        return dp[n-1][6]
