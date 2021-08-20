class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp_a = [[0] * n for _ in range(n)]
        dp_b = [[0] * n for _ in range(n)]
        for i in range(n):
            dp_a[i][i] = piles[i]
        for l in range(1, n):
            for i in range(0, n - l):
                dp_a[i][i + l] = max(piles[i] + dp_b[i + 1][i + l], piles[i + l] + dp_b[i][i + l - 1])
                dp_b[i][i + l] = max(dp_a[i + 1][i + l], dp_a[i][i + l - 1])
        return dp_a[0][n - 1] > sum(piles) // 2
