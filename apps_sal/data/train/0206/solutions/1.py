class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        pre_sum = [nums[0]] * (N + 1)
        pre_sum[-1] = 0
        for i in range(1, N):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
        for i in range(N):
            dp[i][i] = nums[i]
        for l in range(1, N):
            for i in range(N - l):
                dp[i][i + l] = max(pre_sum[i + l] - pre_sum[i - 1] - dp[i + 1][i + l], pre_sum[i + l] - pre_sum[i - 1] - dp[i][i + l - 1])
        return dp[0][N - 1] * 2 >= pre_sum[N - 1]
