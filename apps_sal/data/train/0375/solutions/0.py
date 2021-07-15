class Solution:
     def maximumGap(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums or len(nums) == 1:
             return 0
         sorted_gap=0
         nums=list(set(nums))
         nums.sort()
         for curr in range(len(nums[:-1])):
             gap=nums[curr+1]-nums[curr]
             if gap>sorted_gap:
                 sorted_gap=gap
         
         return sorted_gap
