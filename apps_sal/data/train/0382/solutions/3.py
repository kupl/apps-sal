class Solution:
     def findPeakElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return -1
         start, end = 0, len(nums) - 1
         while start < end:
             mid = start + (end - start) // 2
             if nums[mid] > nums[mid+1]:
                 end = mid
             else:
                 start = mid + 1
         return start
