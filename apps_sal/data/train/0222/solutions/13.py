class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        d = dict()
        for i in range(len(A)):
            for j in range(i):
                if A[i] < 2 * A[j] and A[i] - A[j] in s:
                    d[(A[i], A[j])] = d.get((A[j], A[i] - A[j]), 2) + 1

        return max(d.values() or [0])
