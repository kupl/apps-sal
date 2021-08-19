class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        (h, res) = ({}, 1)
        for i in range(len(A)):
            h[i] = defaultdict(int)
            for j in range(i):
                diff = A[i] - A[j]
                h[i][diff] = h[j][diff] + 1
                res = max(res, h[i][diff])
        return res + 1
