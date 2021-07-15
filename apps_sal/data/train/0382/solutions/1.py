class Solution:
     def findPeakElement(self, nums):
         '''
             Finds the pick in a list of numbers
         '''
         if len(nums) == 0:
             return None
         if len(nums) == 1:
             return 0
         if len(nums) == 2:
             return 0 if nums[0] > nums[1] else 1
         res = list()
         if nums[0] > nums[1]:
             return 0
         if nums[-1] > nums[-2]:
             return len(nums)-1
         for i in range(1, len(nums)-1):
             pre = nums[i-1]
             cur = nums[i]
             nex = nums[i+1]
             if cur > pre and cur > nex:
                 return i
