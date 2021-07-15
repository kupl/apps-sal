class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         counts = {}
         for num in nums:
             if num not in counts:
                 counts[num] = 1
             else:
                 counts[num] += 1
         for k, v in list(counts.items()):
             if v == 1:
                 return k

