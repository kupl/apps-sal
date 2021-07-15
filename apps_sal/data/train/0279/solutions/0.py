class Solution:
     def getPermutation(self, n, k):
         """
         :type n: int
         :type k: int
         :rtype: str
         """
         nums = list("123456789")
         k -= 1
         factor = 1
         for i in range(1, n):
             factor *= i
         res = []
         for i in reversed(list(range(n))):
             res.append(nums[k//factor])
             nums.remove(nums[k//factor])
             if i:
                 k %= factor
                 factor //= i
         return "".join(res)

