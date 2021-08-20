class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        n = m // 3
        slice1 = slices[:m - 1]
        slice2 = slices[1:]
        return max(self.max_sum(slice1, n), self.max_sum(slice2, n))

    def max_sum(self, slices, n):
        m = len(slices)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1:
                    dp[i][j] = slices[0]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i - 1])
        return dp[m][n]
