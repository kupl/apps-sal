class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        maxAns = 10**9 + 7
        krollMax = 15

        dp = [[[0] * (krollMax + 1) for i in range(6)] for j in range(n + 1)]
        # [n+1][6][15+1]

        for i in range(6):
            dp[1][i][1] = 1

        for i in range(2, n + 1):
            for j in range(6):  # current dice num
                for p in range(6):  # previous dice num
                    for k in range(1, krollMax + 1):
                        if k > rollMax[p]:
                            continue
                        if j != p:  # different than previous dice
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][p][k]) % maxAns
                        elif k < rollMax[j]:
                            dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][p][k]) % maxAns
        ans = 0
        for i in range(6):
            for j in range(15 + 1):
                ans += dp[n][i][j]
        return ans % maxAns
