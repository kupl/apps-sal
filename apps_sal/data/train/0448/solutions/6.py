class Solution:
     def checkSubarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         sum = 0
         indices = {0: -1}
         for i in range(len(nums)):
             sum += nums[i]
             if k == 0:
                 l = indices.get(sum)
                 if l is not None and i - l >= 2:
                     return True
                 elif l is None:
                     indices[sum] = i
             else:
                 l = indices.get(sum % k)
                 if l is not None and i - l >= 2:
                     return True
                 elif l is None:
                     indices[sum % k] = i
         return False

