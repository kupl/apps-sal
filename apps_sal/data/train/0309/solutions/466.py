from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        sol = defaultdict(int)
        n = len(A)
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                sol[i, d] = max(sol[i, d], 1 + sol[j, d])
        return max(list(sol.values()), default=0) + 1
