class Solution:
     def maxProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         glo_max = nums[0]
         
         imax = glo_max
         imin = glo_max
         i = 1
         
         while i < len(nums):
             
             
             if nums[i] < 0:
                 temp = imax
                 imax = imin
                 imin = temp
             
             imax = max(nums[i], nums[i] * imax)
             imin = min(nums[i], nums[i] * imin)
             
             
             glo_max = max(glo_max, imax)
             i += 1
         
         return glo_max
