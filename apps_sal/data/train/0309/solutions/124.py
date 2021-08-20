class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        mem = [[0] * 1001 for i in range(len(A))]
        ret = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                mem[i][diff] = mem[j][diff] + 1
                ret = max(ret, mem[i][diff])
        return ret + 1
