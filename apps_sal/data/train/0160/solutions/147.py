class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) == 0:
            return False
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for left in range(n):
            for diff in range(1, n - left):
                right = left + diff
                dp[left][right] = max(piles[left] - dp[left + 1][right], piles[right] - dp[left][right])
        return dp[0][-1] > 0
