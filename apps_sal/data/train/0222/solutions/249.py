from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        A_indices = {a: i for i, a in enumerate(A)}
        lengths = defaultdict(lambda: 2)
        best = 0

        for k in range(len(A) - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if A[i] + A[j] < A[k]:
                    i += 1
                elif A[i] + A[j] > A[k]:
                    j -= 1
                else:
                    lengths[i, j] = lengths[j, k] + 1
                    best = max(best, lengths[i, j])
                    i += 1
                    j -= 1

        return best
