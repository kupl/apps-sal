class Solution:
     def twoSum(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """
         
         # record the sorted index (original position)
         nums_sorted_index = sorted(range(len(nums)), key = lambda k: nums[k])
         # sort the list
         nums.sort()
         for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                 if nums[i]+nums[j] > target:
                     break
                 elif nums[i]+nums[j] == target:
                     return [nums_sorted_index[i], nums_sorted_index[j]]
         print('Can\'t find a match!')
