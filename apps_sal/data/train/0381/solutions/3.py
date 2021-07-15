class Solution:
     def minSubArrayLen(self, s, nums):
         """
         :type s: int
         :type nums: List[int]
         :rtype: int
         """
         i = 0
         j = 0
         _s = 0
         _min = len(nums) + 1
         if len(nums) == 0:
             return 0
         
         while(j < len(nums)):
             _s += nums[j]
             j += 1
             while(_s >= s):
                 _min = min(_min, j - i)
                 _s -= nums[i]
                 i += 1
                 
         if _min > len(nums): return 0
         else: return _min

