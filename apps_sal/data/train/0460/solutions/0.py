class Solution:
     def arrayNesting(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         best = 0
         n = len(nums)
         p = []
         for i in range(len(nums)):
             j = i
             current = 0
             while nums[j] != -1:
                 current += 1
                 n -= 1
                 k = j
                 j = nums[j]
                 nums[k] = -1
             best = max(best,current)
             if n <= best:
                 return best
         return best

