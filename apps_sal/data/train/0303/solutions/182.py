class Solution:
    def maxSumAfterPartitioning(self, A, K):
        n = len(A)
        record = [0] * (n + 1)
        for i in range(n):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                record[i + 1] = max(record[i + 1], record[i - k + 1] + curMax * k)
        return record[n]
