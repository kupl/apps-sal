class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # dp[k][i][j]: # if schemes to achive i profit with j people by assigning first k tasks
        mod = 10 ** 9 + 7
        K = len(group)
        dp = [[[0] * (G + 1) for _ in range(P + 1)] for _ in range(K + 1)]

        dp[0][0][0] = 1

        for k in range(1, K + 1):
            p = profit[k - 1]
            g = group[k - 1]
            for i in range(P + 1):
                for j in range(G + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if j >= g:
                        dp[k][i][j] += dp[k - 1][max(0, i - p)][j - g]
        return sum(dp[K][P]) % mod
