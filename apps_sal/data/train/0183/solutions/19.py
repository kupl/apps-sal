class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1: int = len(nums1)
        n2: int = len(nums2)
        dp: List[List[int]] = [[float('-inf') for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], max(0, dp[i - 1][j - 1]) + nums1[i - 1] * nums2[j - 1])
        return dp[n1][n2]
