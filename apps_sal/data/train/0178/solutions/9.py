class Solution:
     def lengthOfLIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         tails = [0] * len(nums)
         size = 0
         
         for x in nums:
             i = 0
             j = size
             index_to_insert = i
             while i < j:
                 mid = i + (j - i) // 2
                 if tails[mid] < x:
                     i = mid + 1
                 else:
                     j = mid
             
             tails[i] = x
             size = max(size, i + 1)
         
         return size
     

