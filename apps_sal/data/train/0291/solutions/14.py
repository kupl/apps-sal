class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        dp = []
        for i in range(len(arr) + 1):
            dp.append([0, 0])

        ans = 0
        for i in range(1, len(arr) + 1):
            if arr[i - 1] % 2 == 0:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]
            else:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1

            ans += dp[i][1]

        return ans % (pow(10, 9) + 7)
