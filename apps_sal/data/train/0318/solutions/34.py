from functools import *


class Solution(object):
    def maxSizeSlices(self, slices):
        @lru_cache(None)
        def dp(start, end, k):
            if k == 0:
                return 0
            if k == 1:
                return max(slices[start:end + 1])
            if end - start + 1 < k * 2 - 1:
                return -float('inf')
            return max(dp(start + 2, end, k - 1) + slices[start], dp(start + 1, end, k))
        n = len(slices) // 3
        return max(dp(0, len(slices) - 2, n), dp(1, len(slices) - 1, n))
