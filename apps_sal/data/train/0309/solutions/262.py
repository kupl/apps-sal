class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if A is None or not A:
            return 0

        N = len(A)

        f = [{} for _ in range(N)]

        ret = 0

        for i in range(1, N):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in f[j]:
                    f[i][diff] = f[j][diff] + 1
                else:
                    f[i][diff] = 2

                ret = max(ret, f[i][diff])

        return ret
