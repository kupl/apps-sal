class Solution:
     def findMaximumXOR(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         ans = 0
         for bit in range(31, -1, -1) :
             ans = (ans << 1) | 1
             pre = set()
             for n in nums :
                 p = (n >> bit) & ans
                 if p in pre :
                     break
                 pre.add(ans ^ p)
             else :
                 ans ^= 1
         return ans
