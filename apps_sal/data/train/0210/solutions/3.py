class Solution:
     def containsNearbyAlmostDuplicate(self, nums, k, t):
         """
         :type nums: List[int]
         :type k: int
         :type t: int
         :rtype: bool
         """
         
         if t<0:
             return False
         
         w = t+1
         d = {}
         
         for i in range(0, len(nums)):
             m = nums[i]//w
             #print(m,d)
             if m in d:
                 return True
             if m-1 in d and abs(nums[i]-d[m-1])<=t:
                 return True
             if m+1 in d and abs(nums[i]-d[m+1])<=t:
                 return True
             d[m] = nums[i]
             if i>=k:
                 del d[nums[i-k]//w]
                 
         return False

