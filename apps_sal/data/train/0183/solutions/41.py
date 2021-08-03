class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if (max(nums1) < 0 and min(nums2) > 0) or (max(nums2) < 0 and min(nums1) > 0):
            return max(max(nums1) * min(nums2), max(nums2) * min(nums1))

        import functools

        @functools.lru_cache(None)
        def DP(i, j):
            if i == n or j == m:
                return 0
            if nums1[i] * nums2[j] > 0:
                return max(nums1[i] * nums2[j] + DP(i + 1, j + 1), DP(i, j + 1), DP(i + 1, j))
            else:
                return max(DP(i + 1, j + 1), DP(i, j + 1), DP(i + 1, j))

        return DP(0, 0)
