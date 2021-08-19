class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        m = len(piles)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            dp[i][i] = piles[i]
        for length in range(2, m + 1):
            for start in range(0, m, 1):
                end = start + length - 1
                if end >= m:
                    break
                dp[start][end] = max(piles[start] - dp[start + 1][end], piles[end] - dp[start][end - 1])
        return dp[0][m - 1] > 0
