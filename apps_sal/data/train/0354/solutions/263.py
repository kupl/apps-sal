class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        N = n
        faces = len(rollMax)
        MOD = 7 + 10**9
        
        dp = [[0 for _ in range(faces+1)] for _ in range(N+1)]
        
        dp[0][faces] = 1
        
        for i in range(faces):
            dp[1][i] = 1
        
        dp[1][faces] = faces
        
        for i in range(2, N+1):
            for j in range(faces):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    
                    dp[i][j] += dp[i-k][faces] - dp[i-k][j]
            
            dp[i][faces] = sum(dp[i]) % MOD
        
        return dp[N][faces] % MOD
