class Solution:
     def PredictTheWinner(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         def helper(nums, start, end, mem):
             if start == end:
                 return nums[start]
             if (start, end) not in mem:
                 mem[(start, end)] = max(nums[start] - helper(nums, start + 1, end, mem), nums[end] - helper(nums, start, end - 1, mem))
             return mem[(start, end)]
         
         return helper(nums, 0, len(nums) - 1, {}) >= 0
