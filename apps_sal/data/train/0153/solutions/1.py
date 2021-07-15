class Solution:
     def makesquare(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
 #         if sum(nums) % 4 != 0 or len(nums) < 4 or max(nums) > sum(nums) / 4 :
 #             return False
         
 #         nums.sort(reverse=True)      
         
 #         if nums[0] < sum(nums) / 4 and nums[0]  + nums[-1] >  sum(nums):
 #             return False
         
 #         def dfs(nums, pos, target):
 #             if pos == len(nums):
 #                 return True
             
 #             for i in range(4):
 #                 if target[i] >= nums[pos]:
 #                     target[i] -= nums[pos]
 #                     if dfs(nums, pos + 1, target):
 #                         return True
 #                     target[i] += nums[pos]
                     
                     
 #             return False
             
 #         return dfs(nums, 0,  [sum(nums) / 4] * 4)
     
     
         total = sum(nums)
         if total%4 != 0 or len(nums)<4: return False
         size = total/4
         nums.sort(reverse=True)
         used = [False]*len(nums)
         def dfs(i, expect):
             if i >= len(nums): return expect%size == 0
             if used[i]: return dfs(i+1, expect)
             used[i] = True
             if nums[i] == expect: return True
             if nums[i] < expect:
                 expect -= nums[i]
                 available = [j for j in range(i+1, len(nums)) if not used[j]]
                 for x in available:
                     if dfs(x, expect): 
                         return True
             used[i] = False
             return False
         for i in range(len(nums)):
             if not dfs(i, size): return False
         return True
