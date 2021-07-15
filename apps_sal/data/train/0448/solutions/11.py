class Solution:
     def checkSubarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         if k == 0:
             for i in range(len(nums) - 1):
                 if nums[i] == nums[i + 1] == 0:
                     return True
             return False
         if len(nums) <= 1:
             return False
         s = 0
         acc = []
         for n in nums:
             s += n
             s %= k    
             acc.append(s)
         for i in range(1, len(nums)):
             if acc[i] == 0:
                 return True
         return len(set(acc)) != len(acc)

