from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        A_indices = defaultdict(list)
        for i, a in enumerate(A):
            A_indices[a].append(i)
        lengths = defaultdict(lambda: 1)
        best = 0

        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                diff = A[j] - A[i]
                lengths[i, diff] = lengths[j, diff] + 1
                best = max(best, lengths[i, diff])
        return best
