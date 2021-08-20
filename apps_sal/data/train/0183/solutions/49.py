class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1:
            return 0
        cache = [[0 for _ in nums2] for _ in nums1]
        cache[-1][-1] = nums1[-1] * nums2[-1]
        for i in range(len(nums1) - 2, -1, -1):
            cache[i][-1] = max(nums1[i] * nums2[-1], cache[i + 1][-1])
        for i in range(len(nums2) - 2, -1, -1):
            cache[-1][i] = max(nums1[-1] * nums2[i], cache[-1][i + 1])
        for i in range(len(nums1) - 2, -1, -1):
            for j in range(len(nums2) - 2, -1, -1):
                cache[i][j] = max(nums1[i] * nums2[j] + max(cache[i + 1][j + 1], 0), cache[i + 1][j], cache[i][j + 1])
        return cache[0][0]
