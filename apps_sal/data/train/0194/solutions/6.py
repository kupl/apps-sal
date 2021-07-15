class Solution:
     def canPartitionKSubsets(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         total = sum(nums)
         if total%k != 0: return False
         target = total//k
         nums.sort()
         if nums[-1] > target:
             return False
         while nums and nums[-1] == target:
             nums.pop()
             k -= 1
         
         return self.helper(nums, target, [0]*k)
     
     def helper(self, nums, target, dp):
         if not nums: return True
         num = nums.pop()
         for i in range(len(dp)):
             if dp[i] + num <= target:
                 dp[i] += num
                 if self.helper(nums, target, dp):
                     return True
                 dp[i] -= num
             if dp[i] == 0:
                 break
         nums.append(num)
         return False
