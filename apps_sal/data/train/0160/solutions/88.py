class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[[0, 0] for _ in range(len(piles))]for _ in range(len(piles))]
        # print(dp)
        for i in range(len(piles)):
            dp[i][i] = [piles[i], 0]
        # print(dp)
        for i in range(len(piles) - 1, -1, -1):
            for j in range(i, len(piles)):
                if i == j:
                    continue
                a = max(dp[i + 1][j][1] + piles[i], dp[i][j - 1][1] + piles[j])
                dp[i][j] = [a, 0]
                if dp[i][j][0] == dp[i + 1][j][1] + piles[i]:
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][1] = dp[i][j - 1][0]

        if dp[0][len(piles) - 1][0] > dp[0][len(piles) - 1][1]:
            return True
        return False
