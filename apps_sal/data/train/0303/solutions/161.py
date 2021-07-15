class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val = float('-inf')
            for w in range(1, K + 1):
                if i - w < 0: break
                max_val = max(max_val, A[i - w])
                dp[i] = max(dp[i], dp[i - w] + max_val * w)
            
        return dp[-1]

