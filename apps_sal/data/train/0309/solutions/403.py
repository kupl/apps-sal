class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        seqs = {}
        result = 2
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if (A[j], diff, j) in seqs:
                    seqs[A[i], diff, i] = seqs[A[j], diff, j] + 1
                else:
                    seqs[A[i], diff, i] = 2
                result = max(result, seqs[A[i], diff, i])
        return result
