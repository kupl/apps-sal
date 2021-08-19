class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        d = {}
        s = set(A)
        for j in range(n):
            for i in range(j):
                if A[j] - A[i] in s and A[j] - A[i] < A[i]:
                    d[A[i], A[j]] = d.get((A[j] - A[i], A[i]), 2) + 1
        return max(d.values() or [0])
