class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        if nums[0] < 0:
            dp[0][1] = 1
        if nums[0] > 0:
            dp[0][0] = 1
            
        res = dp[0][0]
            
        for i, num in enumerate(nums):
            if i and num < 0:
                dp[i][1] = dp[i-1][0] + 1
                if dp[i-1][1]:
                    dp[i][0] = dp[i-1][1] + 1
            if i and num > 0:
                dp[i][0] = dp[i-1][0] + 1
                if dp[i-1][1]:
                    dp[i][1] = dp[i-1][1] + 1
            res = max(res, dp[i][0])
        return res
