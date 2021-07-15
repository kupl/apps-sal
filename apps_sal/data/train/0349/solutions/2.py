class Solution:
     def deleteAndEarn(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         nums.sort()
         nums.append(-1) #end symbol
         prev_max, cur_max = 0, 0
         prev = -1
         j, i = 0, 0
         while i < len(nums):
             if nums[i] == nums[j]:
                 i += 1
                 continue
             dif = i - j
             temp = dif*nums[j]
             if nums[j] == prev + 1:
                 prev_max, cur_max = cur_max, max(temp + prev_max, cur_max)
             else:
                 prev_max, cur_max = cur_max, temp + cur_max
             prev = nums[j]
             j = i
             i += 1
         return cur_max
