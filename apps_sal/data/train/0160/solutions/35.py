class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        if l == 0:
            return False
        dp = [[0 for i in range(l)] for j in range(l)]

        for i in range(l):
            dp[i][i] = piles[i]

        for i in range(1, l):
            for j in range(l - i):
                dp[j][i + j] = max(piles[j] - dp[i + j][j], piles[i + j] - dp[i + j][i + j - 1])
        return dp[0][l - 1] > 0
