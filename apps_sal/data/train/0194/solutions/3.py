class Solution:
     def canPartitionKSubsets(self, nums, k):
         if sum(nums) % k or len(nums) < k: return False
         if k == 1: return True
         target, used = sum(nums) / k, [False for i in range(len(nums))]
 
         def dfs(start, sum_, k):
             if k == 1:
                 return True
             if sum_ == target:
                 return dfs(0, 0, k - 1)
             for i in range(start, len(nums)):
                 if not used[i] and sum_ < target:
                     used[i] = True
                     if dfs(i + 1, sum_ + nums[i], k):
                         return True
                     used[i] = False
             return False
         return dfs(0, 0, k)
