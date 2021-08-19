class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        if not piles or len(piles) == 0:
            return False
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for length in range(2, len(piles) + 1):
            for i in range(0, len(piles) - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][len(piles) - 1]
