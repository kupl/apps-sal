class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = [collections.defaultdict(lambda: 0) for _ in A]
        res = 1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                v = A[i] - A[j]
                d[j][v] = max(d[i][v] + 1, d[j][v])
                res = max(d[j][v], res)
        return res + 1
