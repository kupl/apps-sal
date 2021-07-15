class Solution:
     def increasingTriplet(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         a, b = float("inf"), float("inf")
         
         for n in nums:
             if n > b:
                 return True
             elif a < n < b:
                 b = n
             elif n < a:
                 a = n
                 
         return False
