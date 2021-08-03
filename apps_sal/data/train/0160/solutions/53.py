class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + piles[i - 1]
        self.dp = [[0 for j in range(n)] for i in range(n)]
        ans = self.solve(piles, 0, n - 1, presum)
        return ans > ans - presum[n]

    def solve(self, piles, i, j, presum):
        if self.dp[i][j] > 0:
            return self.dp[i][j]

        if i == j:
            return piles[i]

        result = piles[i] + presum[j] - presum[i] - self.solve(piles, i + 1, j, presum)
        result = max(result, piles[j] + presum[j - 1] - presum[i - 1] - self.solve(piles, i, j - 1, presum))
        self.dp[i][j] = result
        return result
