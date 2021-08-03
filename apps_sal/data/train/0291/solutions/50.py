class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        dp = [[0 for i in range(2)]for j in range(n)]

        if arr[0] % 2 == 0:
            dp[0][0] = 1
        else:
            dp[0][1] = 1

        for i in range(1, n):
            if arr[i] % 2 == 0:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]
            else:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][1]
        ans = 0
        for i in dp:
            ans = (ans + i[1]) % mod
            # print(i)
        return ans % mod
