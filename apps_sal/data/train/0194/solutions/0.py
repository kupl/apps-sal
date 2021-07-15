class Solution:
     def canPartitionKSubsets(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         target,rem=divmod(sum(nums),k)
         if rem or max(nums)>target: return False
         n=len(nums)
         seen=[0]*n
         nums.sort(reverse=True)
         
         def dfs(k,index,current_sum):
             if k==1:
                 return True
             
             if current_sum==target:
                 return dfs(k-1,0,0)
             for i in range(index,n):
                 if not seen[i] and current_sum+nums[i]<=target:
                     seen[i]=1
                     if dfs(k,i+1,current_sum+nums[i]):
                         return True
                     seen[i]=0
             return False
         
         return dfs(k,0,0)

