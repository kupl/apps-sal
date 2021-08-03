class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if A is None or not A:
            return 0

        N = len(A)

        f = [{} for _ in range(N + 1)]

        ret = 0

        for i in range(2, N + 1):
            for j in range(1, i):
                diff = A[i - 1] - A[j - 1]
                if diff in f[j]:
                    f[i][diff] = f[j][diff] + 1
                else:
                    f[i][diff] = 2

                ret = max(ret, f[i][diff])

        return ret
