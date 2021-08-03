class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return -float('inf')
            return max(nums1[i] * nums2[j], nums1[i] * nums2[j] + dp(i - 1, j - 1), dp(i, j - 1), dp(i - 1, j))
        return dp(len(nums1) - 1, len(nums2) - 1)
