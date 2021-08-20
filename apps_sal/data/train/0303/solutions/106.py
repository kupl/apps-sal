class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        dp[1] = arr[0]
        for i in range(1, len(arr)):
            for j in range(max(0, i - k + 1), i + 1):
                dp[i + 1] = max(dp[i + 1], dp[j] + max(arr[j:i + 1]) * (i - j + 1))
        return dp[-1]
