class Solution:
     def minPatches(self, nums, n):
         """
         :type nums: List[int]
         :type n: int
         :rtype: int
         """
         maxValue = 0
         i = 0
         count = 0
         while maxValue < n:
             # print(i, count, nums[i]-1, maxValue)
             if i >= len(nums):
                 while maxValue < n:
                     maxValue += maxValue +1
                     count += 1
             elif nums[i]-1 > maxValue:
                 maxValue += maxValue +1
                 count += 1
             elif nums[i]-1 == maxValue:
                 maxValue += nums[i]
                 i += 1
             elif nums[i]-1 < maxValue:
                 maxValue += nums[i]
                 i += 1
             
         return count
                 
                 

