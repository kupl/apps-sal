class Solution:
     def jump(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums: return 0
         if len(nums) == 1: return 0
         step, far, maxV = 0, 0, 0
         
         for i in range(len(nums)):
             if i + nums[i] > maxV and i + nums[i] >= len(nums) - 1: return step + 1
             maxV = max(maxV, i + nums[i])
             if i == far:
                 step += 1
                 far = maxV
         return step
