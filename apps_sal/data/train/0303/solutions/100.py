class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(k + 1)]
        rolling_max = -1
        for i in range(0, k):
            rolling_max = max(rolling_max, arr[i])
            dp[i] = rolling_max * (i + 1)
        for i in range(k, len(arr)):
            rolling_max = arr[i]
            for j in range(1, k + 1):
                rolling_max = max(rolling_max, arr[i - j + 1])
                dp[i % (k + 1)] = max(rolling_max * j + dp[(i - j) % (k + 1)], dp[i % (k + 1)])
        return dp[(len(arr) - 1) % (k + 1)]
