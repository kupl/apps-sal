class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        res = 0
        for i in range(n):
            max_val = 0
            for k in range(1, min(K, i + 1) + 1):
                max_val = max(max_val, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + max_val * k)
        return dp[n - 1]
