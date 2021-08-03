class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        return nums[int(n / 2)] if n % 2 == 1 else (nums[int(n / 2)] + nums[int(n / 2) - 1]) / 2.0
