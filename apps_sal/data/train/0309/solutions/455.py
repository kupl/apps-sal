class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        mem = [collections.defaultdict(int) for _ in A]
        res = 1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                v = A[j] - A[i]
                mem[j][v] = max(mem[i][v] + 1, mem[j][v])
                res = max(res, mem[j][v])
        return res + 1
