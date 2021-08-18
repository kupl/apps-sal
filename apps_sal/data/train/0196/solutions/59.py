class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        total = A[0]
        curmax = A[0]
        curmin = A[0]
        maxsum = curmax
        minsum = curmin
        for i in range(1, n):
            curmax = max(curmax + A[i], A[i])
            maxsum = max(maxsum, curmax)
            curmin = min(curmin + A[i], A[i])
            minsum = min(minsum, curmin)
            total += A[i]
        if total == minsum:
            return maxsum
        else:
            return max(maxsum, total - minsum)
