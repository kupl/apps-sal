class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        ans = 0

        if nums[0] % 3 == 0:
            dp[0][0] = nums[0]
        elif nums[0] % 3 == 1:
            dp[0][1] = nums[0]
        else:
            dp[0][2] = nums[0]

        for i in range(1, n):
            if nums[i] % 3 == 0:
                dp[i][0] = dp[i - 1][0] + nums[i]
                if dp[i - 1][1] != 0:
                    dp[i][1] = dp[i - 1][1] + nums[i]
                else:
                    dp[i][1] = dp[i - 1][1]
                if dp[i - 1][2] != 0:
                    dp[i][2] = dp[i - 1][2] + nums[i]
                else:
                    dp[i][2] = dp[i - 1][2]
            elif nums[i] % 3 == 1:
                dp[i][1] = max(dp[i - 1][0] + nums[i], dp[i - 1][1])
                if dp[i - 1][2] != 0:
                    dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + nums[i])
                else:
                    dp[i][0] = dp[i - 1][0]
                if dp[i - 1][1] != 0:
                    dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + nums[i])
                else:
                    dp[i][2] = dp[i - 1][2]
            else:
                dp[i][2] = max(dp[i - 1][0] + nums[i], dp[i - 1][2])
                if dp[i - 1][1] != 0:
                    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
                else:
                    dp[i][0] = dp[i - 1][0]
                if dp[i - 1][2] != 0:
                    dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + nums[i])
                else:
                    dp[i][1] = dp[i - 1][1]
        # print(dp)
        return dp[n - 1][0]
