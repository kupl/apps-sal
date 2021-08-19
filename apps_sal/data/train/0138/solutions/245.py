class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        for i in range(n):
            if nums[i] == 0:
                dp[i] = [0, 0]
            elif i == 0 or nums[i - 1] == 0:
                if nums[i] > 0:
                    dp[i][0] = 1
                else:
                    dp[i][1] = 1
            elif nums[i] > 0:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:
                    dp[i][1] = dp[i - 1][1] + 1
            else:
                if dp[i - 1][1] > 0:
                    dp[i][0] = dp[i - 1][1] + 1
                dp[i][1] = dp[i - 1][0] + 1
        return max((dp[i][0] for i in range(n)))
