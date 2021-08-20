class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        (lens1, lens2) = (len(nums1), len(nums2))
        dp1 = [0 for _ in range(lens1 + 1)]
        dp2 = [0 for _ in range(lens2 + 1)]
        (i, j) = (1, 1)
        while i < lens1 + 1 and j < lens2 + 1:
            if nums1[i - 1] == nums2[j - 1]:
                dp1[i] = max(dp1[i - 1], dp2[j - 1]) + nums1[i - 1]
                dp2[j] = max(dp1[i - 1], dp2[j - 1]) + nums2[j - 1]
                i += 1
                j += 1
            elif nums1[i - 1] < nums2[j - 1]:
                dp1[i] = dp1[i - 1] + nums1[i - 1]
                i += 1
            else:
                dp2[j] = dp2[j - 1] + nums2[j - 1]
                j += 1
        while i < lens1 + 1:
            dp1[i] = dp1[i - 1] + nums1[i - 1]
            i += 1
        while j < lens2 + 1:
            dp2[j] = dp2[j - 1] + nums2[j - 1]
            j += 1
        return max(dp1[-1], dp2[-1]) % (10 ** 9 + 7)
