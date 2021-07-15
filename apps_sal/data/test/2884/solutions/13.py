class Solution(object):
     def combinationSum2(self, candidates, target):
         """
         :type candidates: List[int]
         :type target: int
         :rtype: List[List[int]]
         """
         result = []
         temp = []
         candidates.sort(reverse=True)
 
         self.util(candidates, target, result, temp)
         return result       
 
     def util(self, nums, target, result, temp):
 
         for i in range(len(nums)): 
             if nums[i] == target and (temp + [nums[i]] not in result):
                 result.append(temp + [nums[i]])
             elif nums[i] < target:
                 self.util(nums[i + 1:], target - nums[i], result, temp + [nums[i]])
 
         return 
