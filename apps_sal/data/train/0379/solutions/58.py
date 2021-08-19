class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        dp1 = [0 for i in range(len1 + 1)]
        dp2 = [0 for i in range(len2 + 1)]
        (i, j) = (1, 1)
        while i < len1 + 1 and j < len2 + 1:
            if nums1[i - 1] == nums2[j - 1]:
                dp1[i] = nums1[i - 1] + max(dp1[i - 1], dp2[j - 1])
                dp2[j] = nums2[j - 1] + max(dp1[i - 1], dp2[j - 1])
                i += 1
                j += 1
            elif nums1[i - 1] < nums2[j - 1]:
                dp1[i] = nums1[i - 1] + dp1[i - 1]
                i += 1
            else:
                dp2[j] = nums2[j - 1] + dp2[j - 1]
                j += 1
        while i < len1 + 1:
            dp1[i] = nums1[i - 1] + dp1[i - 1]
            i += 1
        while j < len2 + 1:
            dp2[j] = nums2[j - 1] + dp2[j - 1]
            j += 1
        return max(dp1[-1], dp2[-1]) % (10 ** 9 + 7)
