# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         # max over three different situations
#         # use memoization to avoid repeating. subproblems

from functools import lru_cache


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i == 0 or j == 0:
                return -math.inf
            return max(helper(i - 1, j - 1), helper(i, j - 1), helper(i - 1, j),
                       max(helper(i - 1, j - 1), 0) + nums1[i - 1] * nums2[j - 1])
        return helper(len(nums1), len(nums2))
