from collections import defaultdict


class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        A_indices = {a: i for (i, a) in enumerate(A)}
        lengths = defaultdict(lambda: 2)

        def get_value(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if A[i] + A[j] in A_indices:
                memo[i, j] = 1 + get_value(j, A_indices[A[i] + A[j]])
                self.best = max(self.best, memo[i, j])
            else:
                memo[i, j] = 2
            return memo[i, j]
        best = 2
        for i in range(len(A) - 3, -1, -1):
            for j in range(len(A) - 2, i, -1):
                if A[i] + A[j] in A_indices:
                    lengths[i, j] = 1 + lengths[j, A_indices[A[i] + A[j]]]
                    best = max(best, lengths[i, j])
        return best if best > 2 else 0
