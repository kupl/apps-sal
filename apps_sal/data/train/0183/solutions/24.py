class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        dp[-1][-1] = nums1[-1] * nums2[-1]
        for i in range(len(nums1) - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1], nums1[i] * nums2[-1])
        for i in range(len(nums2) - 2, -1, -1):
            dp[-1][i] = max(dp[-1][i + 1], nums1[-1] * nums2[i])
        for i in range(len(nums1) - 2, -1, -1):
            for j in range(len(nums2) - 2, -1, -1):
                dp[i][j] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1] + nums1[i] * nums2[j], nums1[i] * nums2[j])
        return dp[0][0]
