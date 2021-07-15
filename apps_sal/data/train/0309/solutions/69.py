from collections import OrderedDict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # When adding a new number A[j], we look at all previous numbers A[i]:
        # (1) If A[j] can extend any arithmetic subsequence currently ends at A[i]: LAS += 1
        # (2) Otherwise, LAS = 2
        subseq_lengths = {}
        for j in range(1, len(A)):
            for i in range(j):
                diff = A[j] - A[i]
                if (diff, i) in subseq_lengths:
                    subseq_lengths[diff, j] = subseq_lengths[diff, i] + 1
                else:
                    subseq_lengths[diff, j] = 2
        return max(subseq_lengths.values())
