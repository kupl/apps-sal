class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums)==1:
             return nums[0]
         
         seen=set()
         
         for a in nums:
             if a not in seen:
                 seen.add(a)
         
         s1 = sum(nums)
         s2 = sum(seen)
         
         return int(s2 - (s1-s2)/2)
