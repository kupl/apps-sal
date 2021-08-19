class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # knapsack dp
        # dp[g][p]= n means we have n combinations for we used g people left and made p profit

        dp = [[0] * (P + 1) for i in range(G + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            for i in range(G - g, -1, -1):
                for j in range(P, -1, -1):
                    dp[i + g][min(j + p, P)] += dp[i][j]
            # print(dp)
        res = 0
        for i in range(G + 1):
            res += dp[i][-1]
        return res % (10**9 + 7)
