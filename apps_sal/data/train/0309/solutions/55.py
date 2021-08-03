from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = defaultdict(lambda: defaultdict(lambda: 1))

        for i, a in enumerate(A):
            d[a][0] = 1
            for j in range(i):
                d[a][A[i] - A[j]] = d[A[j]][A[i] - A[j]] + 1
        return max([max(dn.values()) for dn in d.values()])
