class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        f = {}
        maxlen = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                f[i, diff] = f.get((j, diff), 1) + 1
                '\n                if (j, diff) not in f:\n                    f[(i, diff)] = 2\n                else:\n                    f[(i, diff)] = max(f[(i, diff)],  f[(j, diff)] + 1)                \n                '
                maxlen = max(maxlen, f[i, diff])
        return maxlen
