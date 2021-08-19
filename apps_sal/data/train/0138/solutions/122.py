class Solution:

    def getMaxLen2(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        dp = [0] * n
        dp1 = [0] * n
        if nums[0] == 0:
            dp[0] = 0
        elif nums[0] > 0:
            dp[0] = 1
            dp1[0] = 1
            ans = 1
        else:
            dp[0] = -1
            dp1[0] = -1
        for i in range(1, n):
            if nums[i - 1] < 0:
                pre = -1
            else:
                pre = 1
            if nums[i] == 0:
                dp[i] = 0
            elif nums[i] > 0:
                ans = max(ans, 1)
                if dp[i - 1] < 0:
                    dp[i] = dp[i - 1] - 1
                    dp1[i] = dp1[i - 1] - 1
                else:
                    dp[i] = abs(dp[i - 1]) + 1
                    dp1[i] = abs(dp1[i - 1]) + 1
            elif nums[i] < 0:
                dp1[i] = 0
                if dp[i - 1] < 0:
                    dp[i] = abs(dp[i - 1]) + 1
                else:
                    dp[i] = -1 * (dp[i - 1] + 1)
            ans = max(ans, dp[i], dp1[i])
        return ans

    def getMaxLen(self, nums: List[int]) -> int:
        ans1 = self.getMaxLen2(nums)
        ans2 = self.getMaxLen2(nums[::-1])
        return max(ans1, ans2)
