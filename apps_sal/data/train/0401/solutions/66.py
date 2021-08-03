from collections import defaultdict


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: [0, float('-inf'), float('-inf')])

        for i, x in enumerate(nums):
            # print(i, x, dp[i-1][0], dp[i-1][2] + x)
            if x % 3 == 0:
                dp[i][0] = dp[i - 1][0] + x
                dp[i][1] = dp[i - 1][1] + x
                dp[i][2] = dp[i - 1][2] + x

            elif x % 3 == 1:
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + x)
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + x)
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + x)

            elif x % 3 == 2:
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + x)
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + x)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + x)
            # print(dp[i])

        return dp[len(nums) - 1][0]
