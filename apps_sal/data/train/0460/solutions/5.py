class Solution:
     def arrayNesting(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         maxLength = 0
         for i in range(len(nums)):
             length = 0
             j = i
             while nums[j] >= 0:
                 length += 1
                 tmp = nums[j]
                 nums[j] = -1
                 j = tmp
             maxLength = max(maxLength, length)
         return maxLength
