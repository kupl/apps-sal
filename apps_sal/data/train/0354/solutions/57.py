class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        mod = 10**9 + 7
        dp = [[0, 1] + [0] * 14 for i in range(6)]
        for _ in range(n - 1):
            dp2 = [[0] * 16 for i in range(6)]
            for i in range(6):
                for k in range(1, rollMax[i] + 1):
                    for j in range(6):
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % mod
                        else:
                            dp2[j][1] += dp[i][k] % mod
            dp = dp2
        return sum(sum(row) for row in dp) % mod
    
    
        M, K = 6, 15
        dp = [[[0]*(K + 1) for _ in range(M + 1)] for _ in range(n + 1)]
        
        for i in range(1, M+1):
            dp[1][i][1] = 1
            
        for i in range(2, n+1):           
            for j in range(1, M+1):                  
                for m in range(1, M+1):
                    if m != j:
                        dp[i][j][1] += sum(dp[i-1][m][h] for h in range(1, rollMax[m-1] + 1))

                for k in range(1, K):                  
                    dp[i][j][k+1] += dp[i-1][j][k]   
                
        ans = 0
        for m in range(1, M+1):
            for k in range(1, rollMax[m-1] + 1):
                ans += dp[-1][m][k]
                
        return ans % (10**9 + 7)
