class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        ld = [{} for i in range(len(A))]
        ans = 0
        ind = -1
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                if diff in ld[j]:
                    if diff in ld[i]:
                        ld[i][diff] = max(ld[j][diff] + 1, ld[i][diff])
                    else:
                        ld[i][diff] = ld[j][diff] + 1
                elif diff in ld[i]:
                    ld[i][diff] = max(2, ld[i][diff])
                else:
                    ld[i][diff] = 2
                if ld[i][diff] > ans:
                    ind = i
                ans = max(ans, ld[i][diff])
        return ans
