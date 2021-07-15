class Solution:
     def deleteAndEarn(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         count = collections.Counter(nums);#count is a dict [3,4,2]--> {2:1,3:1,4:1}
         prev = None;
         avoid = using = 0;
         for k in sorted(count):
             temp = max(avoid,using)
             if k - 1 != prev:
                 using = k * count[k] + temp
                 avoid = temp
             else:
                 using = k * count[k] + avoid
                 avoid = temp
 
             prev = k
         return max(avoid,using)
