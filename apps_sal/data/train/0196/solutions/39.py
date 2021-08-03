class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mx = float('-inf')
        curr = 0
        for x in A:
            if curr >= 0:
                curr += x
            else:
                curr = x
            mx = max(mx, curr)
        cumSum = []
        curr = 0
        for x in A:
            curr += x
            cumSum.append(curr)
        revCumSum = []
        curr = 0
        for x in reversed(A):
            curr += x
            revCumSum.append(curr)
        for i in range(1, len(A)):
            revCumSum[i] = max(revCumSum[i - 1], revCumSum[i])
        for i in range(len(A) - 1):
            mx = max(mx, cumSum[i] + revCumSum[len(A) - 2 - i])
        mx = max(mx, cumSum[-1])
        return mx
