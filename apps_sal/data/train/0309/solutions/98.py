class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return n
        d = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if (i, diff) in d:
                    d[(j, diff)] = d[(i, diff)] + 1
                else:
                    d[(j, diff)] = 2
        return max(d.values())
