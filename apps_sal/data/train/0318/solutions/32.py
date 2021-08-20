class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        slices1 = slices[0:m - 1]
        slices2 = slices[1:]
        n = m // 3

        def helper(arr, n):
            m = len(arr)
            dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if i == 1:
                        dp[i][j] = arr[0]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + arr[i - 1])
            return dp[m][n]
        return max(helper(slices1, n), helper(slices2, n))
