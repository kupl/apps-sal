class Solution:

    def largestSumOfAverages(self, A, K):
        N = len(A)
        S = [0] * (1 + N)
        for i in range(1, N + 1):
            S[i] = S[i - 1] + A[i - 1]
        B = []
        for i in range(1 + N):
            B.append([0] * (1 + K))
        for m in range(1, N + 1):
            for w in range(1, K + 1):
                if w == 1:
                    B[m][w] = S[m] / m
                    continue
                if m < w:
                    break
                B[m][w] = -1000000
                for e in range(1, m - w + 2):
                    B[m][w] = max(B[m][w], B[m - e][w - 1] + (S[m] - S[m - e]) / e)
        return B[N][K]
