class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        C = len(profit)
        dp = [[[0] * (C + 1) for _ in range(P + 1)] for _ in range(G + 1)]

        for g in range(G + 1):
            dp[g][0][0] = 1

        for g in range(0, G + 1):
            for p in range(0, P + 1):
                for c, [hand_needed, p_gained] in enumerate(zip(group, profit), 1):
                    dp[g][p][c] = dp[g][p][c - 1]
                    if hand_needed <= g:
                        prev_at_least = max(0, p - p_gained)
                        dp[g][p][c] += dp[g - hand_needed][prev_at_least][c - 1]
                    dp[g][p][c] = dp[g][p][c] % 1000000007

        return dp[G][P][-1] % 1000000007

    '''
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)
    '''

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
