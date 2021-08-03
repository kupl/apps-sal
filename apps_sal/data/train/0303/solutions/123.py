class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        n = len(A)
        dp = [0] * (n + 1)

        for i in range(n):
            dp_ix = i + 1
            for k in range(1, K + 1):
                if i - k > -2:
                    dp[dp_ix] = max(dp[dp_ix], max(A[max(0, i - k + 1):i + 1]) * k + dp[dp_ix - k])

        return dp[n]
