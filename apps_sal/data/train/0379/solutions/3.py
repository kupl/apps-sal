class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        (i, j) = (0, 0)
        (a, b) = (0, 0)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                a += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                b += nums2[j]
                j += 1
            else:
                a = b = max(a, b) + nums1[i]
                i += 1
                j += 1
        if i != len(nums1):
            a = max(b, a + sum(nums1[i:]))
        elif j != len(nums2):
            a = max(a, b + sum(nums2[j:]))
        return a % (10 ** 9 + 7)
