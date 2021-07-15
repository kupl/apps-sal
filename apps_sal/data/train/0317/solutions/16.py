class Solution:
    def numPermsDISequence(self, S: str) -> int:
        M = pow(10, 9) + 7
        N = len(S)
        S = '#' + S
        
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            for j in range(i + 1):
                if S[i] == 'D':
                    for k in range(j, i + 1):
                        dp[i][j] += dp[i-1][k]
                else:
                    # S[i] == 'I'
                    for k in range(0, j):
                        dp[i][j] += dp[i-1][k]
        res = 0
        for i in range(N + 1):
            res += dp[N][i]
        return res % M
        
        

