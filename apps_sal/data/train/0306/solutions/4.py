class Solution:
     def combinationSum4(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         
         dp = [0 for x in range(target+1)]
         dp[0] = 1
         for x in range(1, target+1):
             for elem in nums:
                 if x >= elem:
                     dp[x]+=dp[x - elem]
         return dp[-1]
