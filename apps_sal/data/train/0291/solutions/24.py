class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        kMod = int(1000000000.0 + 7)
        n = len(arr)
        dp = [[0] * 2 for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            if arr[i - 1] % 2 != 0:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]
            ans += dp[i][1]
        return ans % kMod
