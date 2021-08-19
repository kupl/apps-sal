class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        def max_possible_score(i, j):
            if j - i == 1:
                return abs(piles[i] - piles[j])
            return max(piles[i] - max_possible_score(i + 1, j), piles[j] - max_possible_score(i, j - 1))
        n = len(piles)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            j = i + 1
            dp[i][j] = abs(piles[i] - piles[j])
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0
