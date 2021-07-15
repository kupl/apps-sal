class Solution:
     def equalSol(self, nums, k):
         if k == 0:
             return False
         d = {}
         for i in range(len(nums)):
             if nums[i] in d.keys() and abs(i - d[nums[i]]) <= k:
                 return True
             else:
                 d[nums[i]] = i
         return False
     
     def containsNearbyAlmostDuplicate(self, nums, k, t):
         """
         :type nums: List[int]
         :type k: int
         :type t: int
         :rtype: bool
         """
         if k == 0:
             return False
         if t == 0:
             return self.equalSol(nums, k)
         for i in range(len(nums)):
             for j in range(1,(k+1)):
                 if (i + j) < len(nums) and abs(nums[i] - nums[i+j]) <= t:
                     return True
                 if (i - j) >= 0 and abs(nums[i] - nums[i-j]) <=t:
                     return True
         return False
