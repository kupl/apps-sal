class Solution:
     def findMedianSortedArrays(self, nums1, nums2):
         """
         :type nums1: List[int]
         :type nums2: List[int]
         :rtype: float
         """
         nums1 = nums1 + nums2
         nums1.sort()
         len_nums1 = len(nums1)
         if len_nums1%2 == 0:
             return float((nums1[int(len_nums1/2)-1]+nums1[int(len_nums1/2)])/2)
         else:
             return float(nums1[int(len_nums1/2)])
         

