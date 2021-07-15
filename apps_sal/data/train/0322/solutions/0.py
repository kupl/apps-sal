class Solution:
     def minPatches(self, nums, n):
         """
         :type nums: List[int]
         :type n: int
         :rtype: int
         """
         res, cur, i = 0, 1, 0
         while cur <= n:
             if i < len(nums) and nums[i] <= cur:
                 cur += nums[i]
                 i += 1
             else:
                 cur *= 2
                 res += 1
         return res
