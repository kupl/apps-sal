class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0]*16 for _ in range(6)]for _ in range(n)]
        
        for i in range(6):
            dp[0][i][1] = 1
            
        MOD = 10**9+7
        
        for i in range(1, n):
            for j in range(6):
                for k in range(6):
                    if j!=k:
                        for l in range(16):
                            dp[i][j][1] += dp[i-1][k][l]
                            dp[i][j][1] %= MOD
                    else:
                        for l in range(rollMax[j]):
                            dp[i][j][l+1] += dp[i-1][k][l]
                            dp[i][j][l+1] %= MOD
        
        ans = 0
        
        for i in range(6):
            for j in range(16):
                ans += dp[n-1][i][j]
                ans %= MOD
        
        return ans
