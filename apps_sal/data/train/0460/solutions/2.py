class Solution:
     def arrayNesting(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
 
         
         dic = set()
         ma = 0
         for i in nums:
             if i not in dic: # not considered
                 set_ = set()
                 while i  not in set_:
                     set_.add(i)
                     i = nums[i]
                 ma = max(ma,len(set_))
                 dic.update(set_)
         return ma
