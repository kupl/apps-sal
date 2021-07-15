from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        if all([x < 0 for x in nums1]) and all([x > 0 for x in nums2]):
            return max(nums1) * min(nums2)
        if all([x > 0 for x in nums1]) and all([x < 0 for x in nums2]):
            return min(nums1) * max(nums2)
        
        @lru_cache(None)
        def dfs(i1, i2):
            if i1 == l1 or i2 == l2:
                return 0
            return max(dfs(i1 + 1, i2), dfs(i1, i2 + 1), nums1[i1] * nums2[i2] + dfs(i1 + 1, i2 + 1))
        
        return dfs(0, 0)

