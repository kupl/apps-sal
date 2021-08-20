class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0 for i in range(len(A) + 1)]
        dp[0] = 0
        dp[1] = A[0]
        for i in range(1, len(A)):
            result = 0
            for j in range(max(0, i - K + 1), i + 1):
                result = max(result, dp[j] + max(A[j:i + 1]) * (i - j + 1))
            dp[i + 1] = result
        return dp[-1]
