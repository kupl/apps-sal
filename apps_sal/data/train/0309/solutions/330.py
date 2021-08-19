from collections import OrderedDict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        max_length = 0
        subseq_lengths = {}
        for j in range(1, len(A)):
            for i in range(j):
                diff = A[j] - A[i]
                if (diff, i) in subseq_lengths:
                    subseq_lengths[diff, j] = subseq_lengths[diff, i] + 1
                else:
                    subseq_lengths[diff, j] = 2
                max_length = max(max_length, subseq_lengths[diff, j])
        return max_length
