from functools import lru_cache


class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        M = 10 ** 9 + 7
        dp = [[[0 for j in range(G + 1)] for i in range(P + 1)] for k in range(len(group) + 1)]
        dp[0][0][0] = 1
        for k in range(1, len(group) + 1):
            for i in range(P + 1):
                for j in range(G + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if j >= group[k - 1]:
                        dp[k][i][j] += dp[k - 1][max(0, i - profit[k - 1])][j - group[k - 1]]
        return sum(dp[len(group)][P]) % M
