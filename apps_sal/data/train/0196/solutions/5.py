class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mx = curr = A[0]
        cumSum = [A[0]]
        for i in range(1, len(A)):
            if curr >= 0:
                curr += A[i]
            else:
                curr = A[i]
            mx = max(mx, curr)
            cumSum.append(cumSum[-1] + A[i])
        revCumSum = []
        curr = 0
        for x in reversed(A):
            curr += x
            if revCumSum:
                revCumSum.append(max(revCumSum[-1], curr))
            else:
                revCumSum.append(curr)
        for i in range(len(A) - 1):
            mx = max(mx, cumSum[i] + revCumSum[len(A) - 2 - i])
        mx = max(mx, cumSum[-1])
        return mx
