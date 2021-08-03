class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        def f(nums1, nums2, i, j, D):

            if i == 0 or j == 0:
                return 0

            elif str([i, j]) in D:
                return D[str([i, j])]

            res = max(nums1[i - 1] * nums2[j - 1] + f(nums1, nums2, i - 1, j - 1, D), f(nums1, nums2, i - 1, j, D), f(nums1, nums2, i, j - 1, D))

            D[str([i, j])] = res

            return res

        D = {}

        res = f(nums1, nums2, len(nums1), len(nums2), D)

        if res == 0 and (max(nums1) < 0 and min(nums2) > 0):
            return max(nums1) * min(nums2)
        elif res == 0 and (max(nums2) < 0 and min(nums1) > 0):
            return max(nums2) * min(nums1)

        return res
