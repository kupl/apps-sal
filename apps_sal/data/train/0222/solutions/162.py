from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        A_indices = {a: i for i, a in enumerate(A)}
        memo = {}
        self.best = 2

        def get_value(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if A[i] + A[j] in A_indices:
                memo[i, j] = 1 + get_value(j, A_indices[A[i] + A[j]])
                self.best = max(self.best, memo[i, j])
            else:
                memo[i, j] = 2
            return memo[i, j]

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                get_value(i, j)

        return self.best if self.best > 2 else 0
