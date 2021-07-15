class Solution(object):
     def combinationSum4(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         dp = [0] + [-1] * target
 
         def calc(target):
             if target == 0:
                 return 1
             if dp[target] >= 0:
                 return dp[target]
             count = 0
             for n in nums:
                 if target - n >= 0:
                     tmp = calc(target - n)
                     if tmp >= 0:
                         count += tmp
             dp[target] = count
             return count
         ans = calc(target)
         print(ans)
         print(dp)
         return ans
 

