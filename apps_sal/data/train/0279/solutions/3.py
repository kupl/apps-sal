class Solution:
     def getPermutation(self, n, k):
         """
         :type n: int
         :type k: int
         :rtype: str
         """
         import math
         nums = list(range(1, n+1))
         ans = ''
         
         k = k - 1 #make sure the divmod result fail in [0, n-1] instead of [1, n]
         while n > 0:
             n = n - 1
             index, k = divmod(k, math.factorial(n))
             ans = ans + str(nums[index])
             nums.remove(nums[index])
             
         return ans 
         

