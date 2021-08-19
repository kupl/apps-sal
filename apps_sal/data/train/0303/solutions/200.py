class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            mx = 0
            for j in range(k):
                if i - j - 1 >= 0:
                    mx = max(mx, arr[i - j - 1])
                    dp[i] = max(dp[i], mx * (j + 1) + dp[i - j - 1])
        return dp[n]
