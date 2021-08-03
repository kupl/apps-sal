class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for period in range(1, n):
            for i in range(n - period):
                j = i + period
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
