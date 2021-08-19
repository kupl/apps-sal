class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        n, m = len(nums1), len(nums2)

        # dp[i][j] max dot product of nums[:i+1][:j+1]
        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = nums1[0] * nums2[0]

        for j in range(1, m):
            dp[0][j] = max(dp[0][j - 1], nums1[0] * nums2[j])

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], nums1[i] * nums2[0])

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(nums1[i] * nums2[j],
                               dp[i - 1][j - 1] + nums1[i] * nums2[j],
                               dp[i - 1][j],
                               dp[i][j - 1],
                               dp[i - 1][j - 1])

        return dp[n - 1][m - 1]
