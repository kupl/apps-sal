class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * len(A)
        dp[0] = A[0]
        partition_max = A[0]
        for x in range(1, K):
            partition_max = max(partition_max, A[x])
            dp[x] = (x + 1) * partition_max
        print(dp)
        for i in range(K, len(dp)):
            partition_max = float('-inf')
            for j in range(K):
                partition_max = max(partition_max, A[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + (j + 1) * partition_max)
        print(dp)
        return dp[-1]
