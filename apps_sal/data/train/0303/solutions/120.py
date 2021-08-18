class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = A[0]
            else:
                for k in range(1, K + 1):
                    if i - k + 1 < 0:
                        break
                    elif i - k + 1 == 0:
                        dp[i] = max(dp[i], max(A[i - k + 1:i + 1]) * k)
                    else:
                        dp[i] = max(dp[i], dp[i - k] + max(A[i - k + 1:i + 1]) * k)
        return dp[n - 1]
