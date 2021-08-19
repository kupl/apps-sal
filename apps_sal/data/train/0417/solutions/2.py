class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
        if size % 2:
            return nums1[size // 2]
        else:
            return (nums1[size // 2] + nums1[size // 2 - 1]) / 2
