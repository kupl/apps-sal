class Solution:

    def profitableSchemes(self, G, P, group, profit):
        dp = [[1] + [0] * G] + [[0] * (G + 1) for _ in range(P)]
        for (p, g) in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(P, i + p)][g + j] += dp[i][j]
        return sum(dp[P]) % (10 ** 9 + 7)
