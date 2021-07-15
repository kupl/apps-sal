class Solution(object):
     def threeSumClosest(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         size = len(nums)
         if size < 3:
             return 0
         nums.sort()
         i = 0 # fix the first index
         ans = nums[0] + nums[1] + nums[size - 1] # ans is used to record the solution
         while i < size - 2:
             tmp = target - nums[i]
             j = i + 1
             k = size - 1
             while j < k:
                 if nums[j] + nums[k] == tmp:
                     return target
                 if nums[j] + nums[k] > tmp:
                     if nums[j] + nums[j + 1] >= tmp:
                         if nums[j] + nums[j + 1] - tmp < abs(ans - target):
                             ans = nums[i] + nums[j] + nums[j + 1]
                         break
                     tmpans = nums[i] + nums[j] + nums[k]
                     if tmpans - target < abs(ans - target):
                         ans = tmpans
                     k -= 1
                 else:
                     if nums[k] + nums[k - 1] <= tmp:
                         if tmp - nums[k] -nums[k - 1] < abs(ans - target):
                             ans = nums[i] + nums[k - 1] + nums[k]
                         break
                     tmpans = nums[i] + nums[j] + nums[k]
                     if target - tmpans < abs(ans - target):
                         ans = tmpans
                     j += 1
             i += 1
             if ans == target:
                 return target
         return ans
