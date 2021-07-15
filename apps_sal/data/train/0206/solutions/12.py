class Solution:
     def PredictTheWinner(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         if not nums: return True
         n = len(nums)
         if n & 1 == 0: return True
         
         dp = [0] * n
         for i in range(n-1, -1, -1):
             for j in range(i, n):
                 if i == j:
                     dp[i] = nums[i]
                 else:
                     dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
         return dp[n-1] >= 0

