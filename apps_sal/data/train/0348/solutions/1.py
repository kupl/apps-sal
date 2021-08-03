class Solution(object):
    def maximumSum(self, arr):
        dp, res = [arr[0], 0], arr[0]
        for i in range(1, len(arr)):
            dp[1] = max(dp[0], dp[1] + arr[i])
            dp[0] = max(arr[i], arr[i] + dp[0])
            res = max(res, dp[0], dp[1])
        return res
