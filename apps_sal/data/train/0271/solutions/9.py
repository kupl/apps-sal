class Solution:
     def canJump(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         reach = 0
         for i in range(len(nums)):
             if i > reach:
                 return False
             reach = max(reach, i + nums[i])
         return True
