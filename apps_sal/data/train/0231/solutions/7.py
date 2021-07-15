class Solution:
     def firstMissingPositive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         i = 0
 
         while i < len(nums):
             tmp = nums[i]
             # exchange to its right idx
             while tmp != i + 1 and tmp > 0 and tmp < len(nums):
                 nums[i] = nums[tmp-1]
                 nums[tmp-1] = tmp
                 if tmp == nums[i]:
                     break
                 tmp = nums[i]
             i += 1
         print(nums)
 
         for i in range(len(nums)):
             if nums[i] != i+1:
                 return i+1
         return len(nums) + 1

