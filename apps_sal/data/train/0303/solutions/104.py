class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        dp[0] = 0
        for i in range(len(arr)):
            dp[i + 1] = dp[i] + arr[i]
            for j in range(k, 1, -1):
                if i - j + 1 >= 0:
                    dp[i + 1] = max(dp[i + 1], dp[i - j + 1] + max(arr[i - j + 1:i + 1]) * j)
        return dp[-1]
