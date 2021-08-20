class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[[0, 0] for _ in range(len(piles))] for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0
        for l in range(1, len(piles)):
            for r in range(len(piles) - l):
                c = r + l
                left = piles[r] + dp[r + 1][c][1]
                right = piles[c] + dp[r][c - 1][1]
                dp[r][c][0] = max(left, right)
                if left > right:
                    dp[r][c][1] = dp[r + 1][c][0]
                else:
                    dp[r][c][1] = dp[r][c - 1][0]
        return dp[0][len(piles) - 1][0] > dp[0][len(piles) - 1][1]
