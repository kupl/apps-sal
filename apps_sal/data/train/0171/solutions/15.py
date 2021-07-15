class Solution:
     def maxProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         maxP = nums[0]
         minP = nums[0]
         p = 1
         result = nums[0] 
         while p < len(nums):
             tmp1 = max(nums[p], nums[p] * maxP, nums[p] * minP)
             tmp2 = min(nums[p], nums[p] * maxP, nums[p] * minP) 
             maxP = tmp1
             minP = tmp2
             print((nums[p], maxP, minP))
             result = max(result, maxP)
             p += 1
         return result
     
 

