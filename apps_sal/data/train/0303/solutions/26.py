class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        maxSum = [0] * n
        for i in range(-1, -K - 1, -1):
            maxSum[i] = max(A[i:]) * -i
        for i in range(n - K - 1, -1, -1):
            ms = 0
            for k in range(1, K + 1):
                ms = max(ms, max(A[i:i + k]) * k + maxSum[i + k])
            maxSum[i] = ms
        return maxSum[0]
