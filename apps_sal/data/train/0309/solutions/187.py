class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res, d = 0, [{} for _ in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in d[j]:
                    d[i][diff] = d[j][diff] + 1
                else:
                    d[i][diff] = 2
                res = max(res, d[i][diff])
        return res

