class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        result = 0
        N = len(A)
        d = collections.defaultdict(int)
        for i in range(1, N):
            for j in range(i):
                diff = A[i] - A[j]
                d[i, diff] = d[j, diff] + 1
                result = max(result, d[i, diff])
        return result + 1
