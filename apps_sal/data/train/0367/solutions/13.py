class Solution:
     def findDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         nums.sort()
         prev = None
         for i in nums:
             if prev == i:
                 return prev
             else:
                 prev = i
