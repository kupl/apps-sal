class Solution(object):
     def canPartitionKSubsets(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         he = sum(nums)
         if he % k != 0:
             return False
         target = he // k
         visit = [0 for _ in range(len(nums))]
         def dfs(k,ind,cur,cnt):
             if k == 0:return True
             if cur == target and cnt > 0:
                 return dfs(k-1,0,0,0)
             for i in range(ind,len(nums)):
                 if not visit[i] and cur+nums[i] <= target:
                     visit[i] = 1
                     if dfs(k,i+1,cur+nums[i],cnt+1):
                         return True
                     visit[i] = 0
             return False
         return dfs(k,0,0,0)
