class Solution:
     def minSubArrayLen(self, s, nums):
         """
         :type s: int
         :type nums: List[int]
         :rtype: int
         """
         if nums is None or len(nums) == 0:
             return 0
         running_sum = [nums[0]]
         for num in nums[1:]:
             running_sum.append(running_sum[-1] + num)
         def sub_sum(i,j):
             to_remove = 0 if i == 0 else running_sum[i-1]
             to_add = 0 if j == 0 else running_sum[j-1]
             return to_add - to_remove
         min_seen = float('inf')
         fast = 0
         slow = 0
         while fast < len(nums):
             while sub_sum(slow, fast) < s and fast < len(nums):
                 fast += 1
             while sub_sum(slow, fast) >= s and slow <= fast:
                 min_seen = min(min_seen, fast - slow)
                 slow += 1
         return 0 if min_seen == float('inf') else min_seen 

