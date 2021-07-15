class Solution:
     def findDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
 #        d = {}
 #        for i in nums:
 #            if i in d:
 #                return i
 #            d[i] = 0
         return (sum(nums)-sum(set(nums))) // (len(nums)-len(set(nums)))
