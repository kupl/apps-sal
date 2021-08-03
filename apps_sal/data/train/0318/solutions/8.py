class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # hard
        m = len(slices)
        n = m // 3
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m - 2, -1, -1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i + 1][j], slices[i] + dp[i + 2][j - 1])
        # print(dp[0][n])
        dp2 = [[0] * (n + 1) for i in range(m + 2)]
        for i in range(m - 1, 0, -1):
            for j in range(1, n + 1):
                dp2[i][j] = max(dp2[i + 1][j], slices[i] + dp2[i + 2][j - 1])

        return max(dp[0][n], dp2[1][n])
