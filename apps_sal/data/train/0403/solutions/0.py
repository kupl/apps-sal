class Solution:
     def increasingTriplet(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         n1 = n2 = float('inf')
         for n in nums:
             if n <= n1:
                 n1 = n
             elif n <= n2:
                 n2 = n
             else:
                 return True
         return False
