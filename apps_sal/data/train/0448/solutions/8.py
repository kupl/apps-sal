class Solution:
     def checkSubarraySum(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         indexs = {}
         indexs[0] = -1
         curr_sum = 0
         for i in range(len(nums)):
             if k != 0:
                 curr_sum += nums[i]
                 modv = curr_sum % k
                 if modv in indexs and i - indexs[modv] > 1:
                     return True
                 if not modv in indexs:
                     indexs[modv] = i
             else:
                 if nums[i] == 0 and i < len(nums) - 1 and nums[i+1] == 0:
                     return True
         return False
