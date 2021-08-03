class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        diff = {}
        for i in range(n):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                if (i, d) in diff:
                    diff[(j, d)] = diff[(i, d)] + 1
                else:
                    diff[(j, d)] = 2
        return max(diff.values())
