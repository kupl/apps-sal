class Solution:
     def jump(self,nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 1:
             return 0
         else:
             step = 0
             pos = 0
             while pos != len(nums) - 1:
                 bestStep = -1
                 bestValue = -1
                 for i in range(nums[pos], 0, -1):
                     if len(nums) - 1 == pos + i:
                         bestStep = i
                         break
                     if (pos + i < len(nums) and nums[pos + i] != 0 and nums[pos + i] + i > bestValue):
                         bestStep = i
                         bestValue = nums[pos + i] + i
                 print(bestStep)
                 pos += bestStep 
                 step += 1
 
             return step
 
 

