class Solution:
     # @param {integer[]} nums
     # @param {integer} k
     # @param {integer} t
     # @return {boolean}
     def containsNearbyAlmostDuplicate(self, nums, k, t):
         if len(nums) == 0 or len(nums) == 1 or k < 1 or t < 0:
             return False
         d = collections.OrderedDict()
         for i in nums:
             key = i if not t else i // t
             for j in (d.get(key - 1), d.get(key), d.get(key + 1)):
                 if j != None and abs(j - i) <= t:
                     return True
             if len(d) == k:
                 d.popitem(False)
             d[key] = i
             
         return False
