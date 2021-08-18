class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i + 1][j + 1] = max([dp[i][j] + nums1[i] * nums2[j], dp[i + 1][j], dp[i][j + 1]])

        return dp[len(nums1)][len(nums2)] if dp[len(nums1)][len(nums2)] > 0 else max([max(nums1) * max(nums2), min(nums1) * min(nums2), max(nums1) * min(nums2), min(nums1) * max(nums2)])
