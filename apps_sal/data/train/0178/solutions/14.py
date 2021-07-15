class Solution:
     def lengthOfLIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         lenLastIdx = [-1]
         for i in range(len(nums)):
             currLen = self.findLen(nums, lenLastIdx, nums[i])
             if len(lenLastIdx) == currLen:
                 lenLastIdx.append(0)
             lenLastIdx[currLen] = i
         return len(lenLastIdx) - 1
     
     def findLen(self, nums, lenLastIdx, val):
         p = 1
         q = len(lenLastIdx)
         while p < q:
             mid = p + (q - p) // 2
             if nums[lenLastIdx[mid]] >= val:
                 q = mid
             else:
                 p = mid + 1
         return p
             
         

