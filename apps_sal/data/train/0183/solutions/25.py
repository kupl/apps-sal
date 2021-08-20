class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        if max(nums2) < 0 and min(nums1) > 0:
            return min(nums1) * max(nums2)
        dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
        for i in range(N):
            for j in range(M):
                dp[i + 1][j + 1] = max(dp[i][j] + nums1[i] * nums2[j], dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
