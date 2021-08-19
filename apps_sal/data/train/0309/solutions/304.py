class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        dd = [[1] * 1001 for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j] + 500
                dd[i][diff] = max(dd[i][diff], dd[j][diff] + 1)
                ans = max(ans, dd[i][diff])
        return ans
