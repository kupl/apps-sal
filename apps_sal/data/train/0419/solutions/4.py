class Solution:
     def bulbSwitch(self, n):
         """
         :type n: int
         :rtype: int
         """
         
         import math
         return math.floor(math.sqrt(n))
         # if n == 0:
         #     return 0
         # else:
         #     nums = [True] * n
         #     if n > 1:
         #         for i in range(2,n):
         #             nums[i-1::i] = [not x for x in nums[i-1::i]]
         #         nums[-1] = (not nums[-1])
         #     return sum(nums)

