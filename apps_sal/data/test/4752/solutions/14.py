class Solution:
     def twoSum(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """
 #         length_nums = len(nums)
         
 #         for i in range(length_nums):
 #             for j in range(i+1, length_nums):
 #                 if nums[i] + nums[j] == target:
 #                     return [i, j]
 
         # dic = {}
         # for i, num in enumerate(nums):
         #     if num in dic:
         #         return [dic[num], i]
         #     else:
         #         dic[target - num] = i
         
         num_dict = {}
         for i, num in enumerate(nums):
             rem = target - num
             if rem in num_dict:
                 return [num_dict[rem], i]
             num_dict[num] = i
         return None
