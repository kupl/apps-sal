from functools import lru_cache


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        @lru_cache(None)
        def dp(i, j, selected):
            if i == n or j == m:
                return 0 if selected else -1000000000

            a = nums1[i] * nums2[j] + dp(i + 1, j + 1, True)
            b = dp(i, j + 1, selected)
            c = dp(i + 1, j, selected)

            return max(a, b, c)

        return dp(0, 0, False)
