class Solution:
     def findPeakElement(self, nums):
         '''
             Finds the pick in a list of numbers
         '''
         length = len(nums)
         if length == 0:
             return None
         if length == 1:
             return (0)
         if length == 2:
             return 0 if nums[0] > nums[1] else 1
 
         for idx in range(0, length):
             value = nums[idx]
             if (idx > 0 and idx < length - 1 and
                 nums[idx + 1] < value and nums[idx - 1] < value):
                     pick = idx
             elif idx == 0 and nums[idx + 1] < value:
                 pick = idx
             elif idx == length - 1 and nums[idx - 1] < value:
                 pick = idx
         return pick
