class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[[piles[i] * (i == j), 0] for j in range(l)] for i in range(l)]
        for d in range(1, l):
            for w in range(l - d):
                x, y = w, w + d
                l1, l2, r1, r2 = dp[x + 1][y] + dp[x][y - 1]
                dp[x][y] = max([l2 + piles[x], l1], [r2 + piles[y], r1])
        return dp[0][-1][0] > dp[0][-1][1]
