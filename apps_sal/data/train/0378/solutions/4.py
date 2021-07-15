class Solution:
     def canPartition(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         
         if len(nums) < 2:
             return False
         
         s = sum(nums)
         if s % 2 != 0:
             return False
         
         s = s // 2
         nums.sort()
         mem = dict()
         
         return self.dp(nums, 0, s, mem)
     
     def dp(self, nums, start, s, mem):
         
         if s == 0:
             return True
         
         if start >= len(nums):
             return False
         
         state = mem.get((start, s), None)
         if state is not None:
             return state
         
         res = False
         if nums[start] > s:
             res = False
             
         else:
             res = self.dp(nums, start+1, s-nums[start], mem) or self.dp(nums, start+1, s, mem)
             
         mem[(start, s)] = res
         return res
