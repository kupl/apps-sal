class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (P + 1) for i in range(G + 1)]
        for i in range(G + 1):
            dp[i][0] = 1
        for g, p in zip(group, profit):
            dp2 = [[0] * (P + 1) for i in range(G + 1)]
            for g1 in range(G + 1):
                for p1 in range(P + 1):
                    dp2[g1][p1] = dp[g1][p1]
                    if g1 >= g:
                        dp2[g1][p1] = (dp2[g1][p1] + dp[g1 - g][max(0, p1 - p)]) % MOD
            dp = dp2
        return dp[G][P]
