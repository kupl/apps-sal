class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        dp[0] = arr[0]
        max_value = arr[0]
        max_sum = arr[0]
        for i in range(1, k):
            max_value = max(max_value, arr[i])
            dp[i] = max_value * (i + 1)
        for i in range(k, len(arr)):
            max_value = 0
            for j in range(k):
                max_value = max(max_value, arr[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + max_value * (j + 1))
        return dp[-1]
