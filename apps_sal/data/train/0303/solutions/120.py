class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = A[0]
            else:
                # A[i-k+1, ..., i-1, i] is a subarray
                # A[0, 1, 2, ..., i-k] is previous chuck with subarray length up to K
                for k in range(1, K+1):
                    if i-k+1 < 0:
                        break
                    elif i-k+1 == 0:
                        dp[i] = max(dp[i], max(A[i-k+1:i+1]) * k)
                    else:
                        dp[i] = max(dp[i], dp[i-k] + max(A[i-k+1:i+1]) * k)
        return dp[n-1]

