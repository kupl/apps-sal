class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        changeSum = 0
        (partial1, partial2) = (0, 0)
        (i, j) = (0, 0)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                print((partial1, partial2))
                changeSum = (changeSum + nums1[i] + max(partial1, partial2)) % (10 ** 9 + 7)
                i += 1
                j += 1
                (partial1, partial2) = (0, 0)
            elif nums1[i] < nums2[j]:
                partial1 += nums1[i]
                i += 1
            else:
                partial2 += nums2[j]
                j += 1
        while i < len(nums1):
            partial1 += nums1[i]
            i += 1
        while j < len(nums2):
            partial2 += nums2[j]
            j += 1
        changeSum = (changeSum + max(partial1, partial2)) % (10 ** 9 + 7)
        return changeSum % (10 ** 9 + 7)
