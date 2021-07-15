class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n+1)]
        MOD = 10 ** 9 + 7
        for i in range(6):
            dp[1][i][1] = 1
            
        for i in range(2, n+1):
            for j in range(6):
                for p in range(6):
                    for k in range(1, rollMax[p]+1):
                        if j != p:
                            dp[i][j][1] = (dp[i][j][1] + dp[i-1][p][k]) % MOD
                        elif k < rollMax[j]:
                            dp[i][j][k+1] = dp[i-1][j][k]
        ans = 0
        for i in range(6):
            for k in range(1, rollMax[i]+1):
                ans = (ans + dp[n][i][k]) % MOD
        return ans
        

