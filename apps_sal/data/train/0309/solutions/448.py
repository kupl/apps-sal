from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = {}
        mval = -1
        for (i, n) in enumerate(A):
            for j in range(i):
                if (j, n - A[j]) not in d:
                    d[i, n - A[j]] = 2
                else:
                    d[i, n - A[j]] = d[j, n - A[j]] + 1
                mval = max(mval, d[i, n - A[j]])
        return mval
