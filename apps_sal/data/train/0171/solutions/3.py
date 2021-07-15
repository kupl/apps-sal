class Solution:
     def maxProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums: return 0
         res = premax = premin = nums[0]
         curmax = curmin = None
         for n in nums[1:]:
             curmax, curmin = max(premax*n, premin*n, n), min(premax*n, premin*n, n)
             premax, premin = curmax, curmin
             res = max(res, curmax)
         return res

