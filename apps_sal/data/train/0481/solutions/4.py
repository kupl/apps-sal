class Solution:
     def threeSumClosest(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         nums = sorted(nums)
         res, diff = None, None
         for first in range(len(nums) - 2):
             if first and nums[first] == nums[first - 1]:
                 continue
                 
             second, third = first + 1, len(nums) - 1
             if diff is None:
                 res = nums[first] + nums[second] + nums[third]
                 diff = abs(res - target)
             while second < third:
                 three_sum = nums[first] + nums[second] + nums[third]
                 if three_sum == target:
                     return target
                 elif three_sum < target:
                     partial = nums[first] + nums[third]
                     while second < third and nums[second] + partial  < target:
                         second += 1
                     tmp = nums[second - 1] + partial
                     if abs(tmp - target) < diff:
                         diff = abs(tmp - target)
                         res = tmp
                 else:
                     partial = nums[first] + nums[second]
                     while second < third and partial + nums[third] > target:
                         third -= 1
                     tmp = partial + nums[third + 1]
                     if abs(tmp - target) < diff:
                         diff = abs(tmp - target)
                         res = tmp
         return res
             

