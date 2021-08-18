class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (G + 1) for _ in range(P + 1)]

        dp[0][0] = 1

        for i in range(len(profit)):
            p = profit[i]
            g = group[i]
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(P, i + p)][j + g] += dp[i][j]

        return sum(dp[-1]) % (10**9 + 7)
