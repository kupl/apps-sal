class Solution:
     def combinationSum4(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         if not nums:
             return 0
         n_nums = len(nums)
         # combinations = [[0]*(n_nums+1)]*(target+max(nums)+3)
         combinations = [[0]*(n_nums+1) for i in range(target+max(nums)+3)]
         for i in range(1, target + 1):
             cur_sum = 0
             for j in range(n_nums):
                 if i == nums[j]:
                     combinations[i][j] = 1
                 else:
                     combinations[i][j] = combinations[i - nums[j]][n_nums]
                 cur_sum += combinations[i][j]
             combinations[i][n_nums]= cur_sum
         return combinations[target][n_nums]
             
         

