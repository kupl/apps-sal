class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = dict()
        for (i, a) in enumerate(A):
            for j in range(i):
                diff = a - A[j]
                if (j, diff) in d:
                    d[i, diff] = d[j, diff] + 1
                else:
                    d[i, diff] = 2
        return max(d.values())
