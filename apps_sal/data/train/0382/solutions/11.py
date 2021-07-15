class Solution:
     def findPeakElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         def bs(nums, i, j):
             if i >= j: return j
             k = (i + j) // 2
             if nums[k] < nums[k+1]:
                 return bs(nums, k+1, j)
             else:
                 return bs(nums, i, k)
                 
         if not nums: return None
         return bs(nums, 0, len(nums)-1)
