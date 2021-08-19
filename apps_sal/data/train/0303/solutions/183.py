class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * (len(A) + 1)
        for i in range(len(A)):
            value = A[i]
            for j in range(1, K + 1):
                if i + j - 1 >= len(A):
                    break
                value = max(A[i + j - 1], value)
                dp[i + j] = max(dp[i] + value * j, dp[i + j])
        return dp[-1]
