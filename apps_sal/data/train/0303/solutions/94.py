class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # dp(i) = max array sum using elements up to index i
        # dp(i) = for j = 1 to k, find max of dp(i-j) + j * max(arr[i-j:i])

        dp = [0 for i in range(len(arr))]
        dp[0] = arr[0]

        for i in range(1, len(arr)):
            ans = 0
            for j in range(1, k + 1):
                if i - j >= 0:
                    ans = max(ans, dp[i - j] + j * max(arr[i - j + 1:i + 1]))
                elif i - j == -1:
                    ans = max(ans, j * max(arr[i - j + 1: i + 1]))

            dp[i] = ans

        return dp[-1]
