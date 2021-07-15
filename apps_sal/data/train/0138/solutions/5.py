class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for i in range(2)]
        for i, x in enumerate(nums):
            if x > 0:
                dp[0][i+1] = dp[0][i] + 1
                if dp[1][i] > 0:
                    dp[1][i+1] = dp[1][i] + 1
            elif x < 0:
                if dp[1][i] > 0:
                    dp[0][i+1] = dp[1][i] + 1
                dp[1][i+1] = dp[0][i] + 1
            else:
                dp[0][i+1] = dp[1][i+1] = 0
                
        # print(dp)
        return max(dp[0])

