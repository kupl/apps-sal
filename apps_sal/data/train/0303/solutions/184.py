class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            m = -float('inf')
            d = 0
            while d < k and i - d > 0:
                m = max(m, arr[i - 1 - d])
                dp[i] = max(dp[i], dp[i - d - 1] + m * (d + 1))
                d += 1
        return dp[n]
