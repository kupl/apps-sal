from functools import lru_cache


class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @lru_cache(None)
        def solve(i, j, c):
            if i == len(nums1) or j == len(nums2):
                if c:
                    return 0
                return float('-inf')
            return max(solve(i + 1, j, c), solve(i, j + 1, c), nums1[i] * nums2[j] + solve(i + 1, j + 1, True))
        return solve(0, 0, False)
