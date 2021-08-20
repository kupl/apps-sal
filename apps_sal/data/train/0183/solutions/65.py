import numpy as np


class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        INF = int(1000000000.0)
        (n, m) = (len(nums1), len(nums2))
        DP = np.ones((n + 1, m + 1), dtype=int) * -INF
        for a in range(n):
            for b in range(m):
                el = nums1[a] * nums2[b]
                diag = DP[a, b]
                DP[a + 1, b + 1] = max(el, DP[a, b + 1], DP[a + 1, b], diag, diag + el)
        return DP[-1, -1]
