class Solution:
     def firstMissingPositive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         minSet = set()
         maxSet = set()
         nums = set(nums)
         for num in nums:
 
             if num > 0:
                 if num + 1 in minSet:
                     minSet.remove(num + 1)
                     minSet.add(num)
                     if num - 1 in maxSet:
                         maxSet.remove(num - 1)
                         minSet.remove(num)
                 elif num - 1 in maxSet:
                     maxSet.remove(num - 1)
                     maxSet.add(num)
                     if num + 1 in minSet:
                         maxSet.remove(num)
                         minSet.remove(num + 1)
                 else:
                     minSet.add(num)
                     maxSet.add(num)
                 # print("min set:", minSet)
                 # print("max set:", maxSet)
         if len(minSet) == 0 or len(maxSet) == 0:
             return 1
         return min(maxSet) + 1 if min(minSet) == 1 else 1
