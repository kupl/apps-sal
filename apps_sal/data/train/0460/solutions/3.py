class Solution:
     def arrayNesting(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         ans, step, n = 0, 0, len(nums)
         signal = [False] * n
         for i in range(n):
             while not signal[i]:
                 signal[i] = True
                 step += 1
                 i = nums[i]
                 ans = max(ans, step)
             step = 0
         return ans
