class Solution:
     def canJump(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         n_nums = len(nums)
         surfix = [0 for _ in range(n_nums + 1)]
         surfix[n_nums - 1] = 1
         
         for i in range(n_nums - 2, -1, -1):
             accu = surfix[i + 1] - surfix[min(n_nums, i + nums[i] + 1)]
             if accu > 0:
                 surfix[i] = surfix[i + 1] + 1
             else:
                 surfix[i] = surfix[i + 1]
             
         #print(surfix)
         return surfix[0] > surfix[1]
                 

