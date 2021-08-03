class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        if arr[n - 1] & 1:
            dp[n - 1][1] = 1
        else:
            dp[n - 1][0] = 1

        for i in range(n - 2, -1, -1):
            if arr[i] & 1:
                dp[i][1] = (dp[i + 1][0] + 1) % mod
                dp[i][0] = dp[i + 1][1]
            else:
                dp[i][1] = dp[i + 1][1]
                dp[i][0] = (dp[i + 1][0] + 1) % mod

        ans = 0
        for i in range(n):
            ans += dp[i][1]

        return ans % mod
