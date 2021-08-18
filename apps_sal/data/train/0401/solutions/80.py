class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0, 0, 0] for i in range(n)]

        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
            dp[i][2] = dp[i - 1][2]

            if nums[i] % 3 == 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + nums[i])
                if dp[i - 1][1]:
                    dp[i][1] = max(dp[i][1], dp[i - 1][1] + nums[i])
                if dp[i - 1][2]:
                    dp[i][2] = max(dp[i][2], dp[i - 1][2] + nums[i])

            elif nums[i] % 3 == 1:
                if dp[i - 1][2]:
                    dp[i][0] = max(dp[i][0], dp[i - 1][2] + nums[i])

                dp[i][1] = max(dp[i][1], dp[i - 1][0] + nums[i])
                if dp[i - 1][1]:
                    dp[i][2] = max(dp[i][2], dp[i - 1][1] + nums[i])
            else:
                if dp[i - 1][1]:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] + nums[i])
                if dp[i - 1][2]:
                    dp[i][1] = max(dp[i][1], dp[i - 1][2] + nums[i])
                dp[i][2] = max(dp[i][2], dp[i - 1][0] + nums[i])

        return dp[n - 1][0]
