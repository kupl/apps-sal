class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        preSum = [0]
        acc = 0
        for i in range(len(A)):
            acc += A[i]
            preSum.append(acc)
        mx = 0
        for i in range(L, len(preSum)):
            for j in range(i, len(preSum) - M):
                left = preSum[i] - preSum[i - L]
                right = preSum[j + M] - preSum[j]
                mx = max(mx, left + right)
        for i in range(M, len(preSum)):
            for j in range(i, len(preSum) - L):
                left = preSum[i] - preSum[i - M]
                right = preSum[j + L] - preSum[j]
                mx = max(mx, left + right)
        return mx
