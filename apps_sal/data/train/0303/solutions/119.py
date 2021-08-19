class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * N
        dp[0] = A[0]
        for i in range(1, N):
            for j in range(0, min(K, i + 1)):
                current_subarray = A[i - j:i + 1]
                if i >= K:
                    dp[i] = max(dp[i], dp[i - j - 1] + max(current_subarray) * (j + 1))
                else:
                    dp[i] = max(dp[i], max(current_subarray) * (j + 1))
        return dp[-1]
        (0, 1)
        (1, 1)
