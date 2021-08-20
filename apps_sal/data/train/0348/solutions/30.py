class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('-inf')] * 2 for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = float('-inf')
        for i in range(1, n):
            dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i])
            dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0])
        ans = float('-inf')
        for i in range(n):
            for j in range(2):
                ans = max(ans, dp[i][j])
        return ans
