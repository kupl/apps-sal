import numpy as np


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        M = np.zeros((len(nums1), len(nums2)), dtype=np.int)

        M[0][0] = nums1[0] * nums2[0]
        for i in range(1, len(nums1)):
            M[i][0] = max(M[i - 1][0], nums1[i] * nums2[0])
        for j in range(1, len(nums2)):
            M[0][j] = max(M[0][j - 1], nums1[0] * nums2[j])

        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                M[i][j] = max(M[i - 1][j - 1] + nums1[i] * nums2[j], M[i][j - 1], M[i - 1][j], nums1[i] * nums2[j])
        return M[-1][-1]
