class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) < 3:
            return len(A)

        n = len(A)

        diff_c = collections.Counter()

        for i in range(n):
            for j in range(i):
                if diff_c[(j, A[i] - A[j])] == 0:
                    diff_c[(i, A[i] - A[j])] = 2
                else:
                    diff_c[(i, A[i] - A[j])] = diff_c[(j, A[i] - A[j])] + 1

        return max(diff_c.values())
