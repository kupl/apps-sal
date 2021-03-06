from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = defaultdict(int)
        maxVal = 2
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if (j, diff) not in d:
                    d[i, diff] = 2
                else:
                    d[i, diff] = d[j, diff] + 1
        return max(d.values())
