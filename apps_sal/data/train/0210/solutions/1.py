class Solution:
     def containsNearbyAlmostDuplicate(self, nums, k, t):
         """
         :type nums: List[int]
         :type k: int
         :type t: int
         :rtype: bool
         """
         nums2 = [(n, i) for i, n in enumerate(nums)]
         nums2 = sorted(nums2)
         print(nums2)
         for i in range(1, len(nums2)):
             j = i-1
             a, n = nums2[j]
             b, m = nums2[i]
             while abs(a-b) <= t:
                 if abs(n-m) <= k:
                     return True
                 j -= 1
                 if j < 0:
                     break
                 a, n = nums2[j]
 
         return False
             

