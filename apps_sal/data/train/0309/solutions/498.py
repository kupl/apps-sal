import itertools


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                check = (i, A[j] - A[i])
                if check in d:
                    d[(j, A[j] - A[i])] = d[check] + [A[j]]
                else:
                    d[(j, A[j] - A[i])] = [A[i], A[j]]
        return len(max([i for i in list(d.values())], key=len))
