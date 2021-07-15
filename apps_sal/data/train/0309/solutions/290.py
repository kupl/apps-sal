class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        h = {}
        h[0] = defaultdict(int)
        res = 1
        for i in range(1, len(A)):
            h[i] = defaultdict(int)
            for j in range(i):
                diff = A[i] - A[j]
                h[i][diff] = h[j][diff] + 1
                res = max(res, h[i][diff])
        return res + 1
