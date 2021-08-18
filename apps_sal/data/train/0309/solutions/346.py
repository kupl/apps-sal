class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        f = {}
        maxlen = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                f[(i, diff)] = f.get((j, diff), 1) + 1
                '''
                if (j, diff) not in f:
                    f[(i, diff)] = 2
                else:
                    f[(i, diff)] = max(f[(i, diff)],  f[(j, diff)] + 1)                
                '''
                maxlen = max(maxlen, f[(i, diff)])

        return maxlen
