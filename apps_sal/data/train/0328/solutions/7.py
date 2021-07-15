class Solution:
     def find132pattern(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         if len(nums) < 3:
             return False
         minx = nums[0]
         seg = [(nums[0], nums[0])]
         for x in nums[1:]:
             while seg and seg[-1][1] <= x:
                 seg.pop()
             if seg and x > seg[-1][0]:
                 return True
             minx = min(minx, x)
             seg.append((minx, x))
         return False
