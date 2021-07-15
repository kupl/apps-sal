class Solution:
     def checkSubarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
 
         if not nums or len(nums) < 2:
             return False
 
         k = abs(k)
         n = len(nums)
         d = {0:-1}
         sum = 0
         for i in range(n):
             sum += nums[i]
             key = sum % k if k > 0 else sum
             
             if key not in d:
                 d[key] = i
             elif i >= d[key] + 2:
                 print(d[key] + 1, i)
                 return True
 
         return False
