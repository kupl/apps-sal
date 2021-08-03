class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        d = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                d[j, A[j] - A[i]] = d.get((i, A[j] - A[i]), 1) + 1
        return max(d.values())
