class Solution:
     def findPeakElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         return self.helper(nums, 0, len(nums) - 1)
     
     def helper(self, nums, start, end):
         if start == end:
             return start
         mid = (end + start) // 2
         if nums[mid] > nums[mid + 1]:
             return self.helper(nums, start, mid)
         else:
             return self.helper(nums, mid + 1, end)
