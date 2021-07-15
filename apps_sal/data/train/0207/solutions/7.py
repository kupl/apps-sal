class Solution:
     def largestNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: str
         """
         def lexic_comp(a, b):
             ab = str(a) + str(b)
             ba = str(b) + str(a)
             if ab > ba:
                 return -1
             elif ba > ab:
                 return 1
             return 0
         
         import functools
         
         nums.sort(key=functools.cmp_to_key(lexic_comp))
         
         return str(int(''.join(map(str, nums))))

