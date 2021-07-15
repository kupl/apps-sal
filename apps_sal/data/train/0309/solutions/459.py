from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        # lengths of AM seqs after i with a diff d
        mem = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                mem[i][d] = max(1 + mem[j].get(d, 0), mem[i][d])
                res = max(mem[i][d], res)
        return res + 1
