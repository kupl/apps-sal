class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j = i - 1
            mx = -float('inf')
            while i - j <= k and j >= 0:
                mx = max(mx, arr[j])
                dp[i] = max(dp[i], dp[j] + mx * (i - j))
                j -= 1
        return dp[n]
