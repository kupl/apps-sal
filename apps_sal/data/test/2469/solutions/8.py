class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: List[int]
         """
         ret = []
         least = len(nums) / 3
         h = {}
         for n in nums:
             if n in list(h.keys()):
                 h[n] += 1
             else:
                 h[n] = 1
                 
             if h[n] > least and n not in ret:
                 ret.append(n)
                 
         return ret
             

