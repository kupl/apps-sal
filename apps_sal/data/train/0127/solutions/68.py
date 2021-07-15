class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0 for _ in range(len(profit) + 1)] for _ in range(P + 1)] for _ in range(G + 1)]
        if P == 0:
            dp[1][0][0] = 1
        
        for i in range(1, G + 1):
            for j in range(0, P + 1):
                for k in range(1, len(profit) + 1):
                    dp[i][j][k] = dp[i][j][k - 1]
                    if profit[k-1] >= j and i >= group[k - 1]:
                        dp[i][j][k] += 1
                    if i > group[k - 1]:
                        remaining_g = i - group[k - 1]
                        remaining_p = max(0, j - profit[k-1])
                        dp[i][j][k] += dp[remaining_g][remaining_p][k - 1]
                    dp[i][j][k] %= (10 ** 9 + 7)

        return dp[G][P][len(profit)]
