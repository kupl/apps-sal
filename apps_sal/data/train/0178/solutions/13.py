class Solution:
     def lengthOfLIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if nums == []:
             return 0
         dp = []
         for i, num in enumerate(nums):
             if i == 0 or num > dp[-1]:
                 dp.append(num)
             elif num < dp[0]:
                 dp[0] = num
             else:
                 low, high = 0, len(dp) - 1
                 while(low < high):
                     mid = (low + high)//2
                     mid_num = dp[mid]
                     if num > mid_num:
                         low = mid + 1
                     else:
                         high = mid
                 dp[low] = num
         return len(dp)

