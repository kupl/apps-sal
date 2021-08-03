class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[(0, 0)] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = (piles[i], 0)

        for diff in range(1, len(piles)):
            for j in range(len(piles) - diff):
                i = diff + j
                left = dp[j + 1][i][1] + piles[j]
                right = dp[j][i - 1][1] + piles[i]
                if left > right:
                    dp[j][i] = (left, dp[j + 1][i][0])
                else:
                    dp[j][i] = (right, dp[j][i - 1][0])

        return dp[0][-1][0] > dp[0][-1][1]
