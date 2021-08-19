class Solution:

    def maxSumAfterPartitioning(self, arr, k):
        if not arr:
            return 0
        dp = [0] * len(arr)
        for i in range(len(arr)):
            for j in range(k):
                if i - j < 0:
                    continue
                max_val = max(arr[i - j:i + 1])
                if i - j == 0:
                    total = max_val * (j + 1)
                else:
                    total = dp[i - j - 1] + max_val * (j + 1)
                dp[i] = max(dp[i], total)
        return dp[-1]
