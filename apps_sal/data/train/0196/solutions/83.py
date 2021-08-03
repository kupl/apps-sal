class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        B = A.copy()
        for i in range(1, len(B)):
            if B[i - 1] > 0:
                B[i] += B[i - 1]
        maxsum = max(B)
        C = A.copy()
        for i in range(1, len(C)):
            if C[i - 1] < 0:
                C[i] += C[i - 1]
        minsum = min(C)
        if minsum == sum(A):
            return max([maxsum, max(A)])
        return max([maxsum, sum(A) - minsum])
