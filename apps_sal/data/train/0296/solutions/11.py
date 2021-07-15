class Solution:
     def findMin(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         min_n = nums[0]
         for n in nums:
             if n < min_n:
                 min_n = n
         return min_n

