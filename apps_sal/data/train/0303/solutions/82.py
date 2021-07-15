class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for w in range(1, K + 1):
                if i - w < 0: break
                dp[i] = max(dp[i], dp[i - w] + max(A[i - w:i]) * w)
            
        return dp[-1]

