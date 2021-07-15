class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        dp = [[0] * (faces+1) for _ in range(n+1)]
        mod = 10 ** 9 + 7
        dp[0][faces] = 1
        
        for i in range(faces):
            dp[1][i] = 1
            
        dp[1][faces] = faces
        for i in range(2, n+1):
            for j in range(faces):
                for k in range(1, rollMax[j]+1):
                    if i - k < 0:
                        break
                    dp[i][j] += (dp[i-k][faces] - dp[i-k][j]) % mod
            dp[i][faces] = sum(dp[i][:faces]) % mod
        return dp[n][faces] % mod
                    

