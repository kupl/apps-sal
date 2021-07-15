class Solution:
     def increasingTriplet(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         if len(nums) < 3:
             return False
         
         tails = [-2147483647, nums[0]]
         
         for n in nums[1:]:
             for i in range(len(tails) - 1, -1, -1):
                 if n > tails[i]:
                     if len(tails) <= i + 1:
                         tails.append(n)
                     elif n < tails[i+1]:
                         tails[i+1] = n
                     
                     if len(tails) == 4:
                         return True
                 print(tails)
         
         return False
