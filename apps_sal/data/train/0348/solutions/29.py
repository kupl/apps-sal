class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(arr))]
        dp[0][0] = arr[0]
        dp[0][1] = arr[0]
        ans = max(dp[0])
        for i in range(1, len(arr)):
            dp[i][0] = max(dp[i - 1][0] + arr[i], dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][1] + arr[i], arr[i])
            ans = max(ans, dp[i][0], dp[i][1])
        return ans
