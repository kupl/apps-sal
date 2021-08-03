class Solution:
    # dp[i][j][k] c!=k dp[i-1][j-1][c]
    # dp[i][j][k]
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # from inner to outer
        dp = [[[0 for k in range(16)] for j in range(6)] for i in range(n)]
        # print(len(dp),len(dp[0]),len(dp[0][0]))
        mod = 1e9 + 7
        for i in range(6):
            dp[0][i][1] = 1
        # print(dp)
        for i in range(1, n):
            for j in range(6):
                for k in range(1, 16):
                    if k == 1:
                        for jj in range(6):
                            for kk in range(1, rollMax[jj] + 1):
                                if j != jj:
                                    # print(kk,jj,i,j,k)
                                    try:
                                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][jj][kk]) % mod
                                    except IndexError as e:
                                        print((kk, jj, i, j, k))
                    else:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
        res = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                res = (res + dp[n - 1][j][k]) % mod
        return int(res)
