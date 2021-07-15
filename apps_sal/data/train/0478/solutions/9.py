class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return 0
         
         seen = set([])
         counts = {}
         for num in nums:
             if num in seen:
                 counts[num] += 1
             else:
                 counts[num] = 1
                 seen.add(num)
         
         for key in counts:
             if counts[key] == 1:
                 return key
         
         return 0
