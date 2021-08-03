class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        def kadane(A):
            ts = A[0]
            ms = A[0]
            for i in range(1, len(A)):
                ts = max(A[i], ts + A[i])
                ms = max(ms, ts)
            return ms
        x = kadane(A)
        for i in range(len(A)):
            A[i] *= -1
        s = sum(A)
        y = kadane(A)
        if y == s:
            y = -1e10
        else:
            y = -s + y
        return max(x, y)
