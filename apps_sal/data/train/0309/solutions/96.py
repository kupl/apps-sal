from collections import OrderedDict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        subseq_lengths = {}
        for j in range(1, len(A)):
            for i in range(j):
                diff = A[j] - A[i]
                subseq_lengths[diff, j] = subseq_lengths.get((diff, i), 1) + 1
        return max(subseq_lengths.values())
