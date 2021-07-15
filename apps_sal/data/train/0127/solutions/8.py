class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(group)
        dp = [[0] * (G + 1) for _ in range(P + 1)]
        dp[0][0] = 1
        # Key point is to iterate reversely, like knapsack problem
        for g, p in zip(group, profit):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[-1]) % mod

