class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n, M = len(group), 10**9 + 7
        dp = [[0] * (P + 1) for _ in range(G + 1)]  # dp[i][j] is the # of schemes of i people and j profit
        dp[0][0] = 1
        for k in range(1, n + 1):
            g, p = group[k - 1], profit[k - 1]
            for i in range(G, g - 1, -1):
                for j in range(P, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % M

        res = 0
        for i in range(G + 1):
            res = (res + dp[i][P]) % M

        return res
