class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[[0, 0] for _ in range(l + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):
            dp[i][i][0] = piles[i - 1]
        for i in range(l + 1, -1, -1):
            for j in range(i + 1, l + 1):
                left = piles[i - 1] + dp[i + 1][j][1]
                right = piles[j - 1] + dp[i][j - 1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[1][l][0] > dp[1][l][1]
