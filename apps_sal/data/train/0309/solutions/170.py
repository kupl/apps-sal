class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:

        n = len(A)
        DP = {}
        for i in range(1, len(A)):
            for j in range(0, i):
                if (j, A[i] - A[j]) in DP:
                    DP[(i, A[i] - A[j])] = DP[(j, A[i] - A[j])] + 1
                else:
                    DP[(i, A[i] - A[j])] = 2

        return max(DP.values())

        n = len(A)
        dp = {}
        for i in range(n):
            for j in range(i + 1, n):
                dif = A[j] - A[i]
                if (i, dif) in dp:
                    dp[(j, dif)] = dp[(i, dif)] + 1
                else:
                    dp[(j, dif)] = 2
        return max(dp.values())
