class Solution:
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p_gained, g_needed in zip(profit, group):
            ndp = [[0] * (G + 1) for i in range(P + 1)]
            for p in range(P + 1):
                for g in range(0, G + 1):
                    ndp[p][g] += dp[p][g]
                    if g >= g_needed:
                        ndp[p][g] += dp[max(p - p_gained, 0)][g - g_needed]
            dp = ndp
        return sum(dp[P]) % (10**9 + 7)

    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p_gained, g_needed in zip(profit, group):
            for p in range(P, -1, -1):
                for g in range(G, g_needed - 1, -1):
                    dp[p][g] += dp[max(p - p_gained, 0)][g - g_needed]
        return sum(dp[P]) % (10**9 + 7)
