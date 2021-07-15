class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0 for i in range(2)]  for j in  range(len(nums) + 1)]
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                dp[i + 1][0] = dp[num][1] = 0
            elif num > 0:
                dp[i + 1][0] = dp[i][0] + 1
                dp[i + 1][1] = dp[i][1] + 1 if dp[i][1] else 0
            else:
                dp[i + 1][0] = dp[i][1] + 1 if dp[i][1] else 0
                dp[i + 1][1] = dp[i][0] + 1
            res = max(res, dp[i + 1][0])
        return res
