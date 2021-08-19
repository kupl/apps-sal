class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        (m, n) = (len(nums1), len(nums2))
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = nums1[i] * nums2[j]
                if i and j:
                    dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[m - 1][n - 1]
