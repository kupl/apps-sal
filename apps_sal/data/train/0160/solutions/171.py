class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        start = len(piles) - 1
        while start >= 0:
            end = start + 1
            while end < len(piles):
                dp[start][end] = max(piles[start] - dp[start + 1][end], piles[end] - dp[start][end - 1])
                end += 1
            start -= 1
        return dp[0][len(piles) - 1] >= 0
