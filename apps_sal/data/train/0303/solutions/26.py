class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        # maxSum[i] = max(A[i] + maxSum[i+1], max(A[i], A[i+1]) + maxSum[i+2], max(A[i], A[i+1], A[i+2], maxSum[i+3]))
        maxSum = [0] * n;
        for i in range(-1, -K-1, -1):
            maxSum[i] = max(A[i:])*(-i)
        for i in range(n-K-1, -1, -1):
            ms = 0
            for k in range(1, K+1):
                ms = max(ms, max(A[i:i+k]) * k + maxSum[i+k])
                # print(i,k,ms)
            maxSum[i] = ms
        # print(maxSum)
        return maxSum[0]

