class Solution:
     def PredictTheWinner(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         l = len(nums)
         memo = [[None] * l for _ in range(l)]
         def predict(start, end, memo):
             if start == end:
                 return nums[start]
             if memo[start][end]:
                 return memo[start][end]
             one = nums[start] - predict(start + 1, end, memo)
             two = nums[end] - predict(start, end - 1, memo)
             memo[start][end] = max(one, two)
             return memo[start][end]
         
         return predict(0, len(nums) - 1, memo) >= 0
