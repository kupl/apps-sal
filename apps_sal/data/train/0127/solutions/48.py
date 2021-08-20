class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0 for _ in range(P + 1)] for _ in range(G + 1)] for _ in range(len(profit) + 1)]
        dp[0][-1][-1] = 1
        mod = int(1000000000.0 + 7)
        for i in range(1, len(profit) + 1):
            for j in range(G, -1, -1):
                for k in range(P, -1, -1):
                    dp[i][j][k] = dp[i - 1][j][k]
                for k in range(P, -1, -1):
                    if j + group[i - 1] <= G:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j + group[i - 1]][min(k + profit[i - 1], P)]) % mod
        res = 0
        for j in range(G + 1):
            res = (res + dp[-1][j][0]) % mod
        return res
