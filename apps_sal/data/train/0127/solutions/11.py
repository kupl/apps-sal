class Solution:
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            dp2 = [i[:] for i in dp]
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp2[min(i + p, P)][j + g] += dp[i][j]
            dp = dp2
        return sum(dp[P]) % (10**9 + 7)
