class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        di = {}
        for i in range(1, len(A)):
            for j in range(i):
                d = A[i] - A[j]
                if (j, d) in di:
                    di[i, d] = di[j, d] + 1
                else:
                    di[i, d] = 2
        return max(di.values())
