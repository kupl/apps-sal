class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        P = [0] * (N + 1)
        for i in range(1, N + 1):
            P[i] = P[i - 1] + A[i - 1]

        Table = [(P[N] - P[i]) / (N - i) for i in range(N)]
        for k in range(2, K + 1):
            for i in range(K - k, N - (k - 1)):
                Table[i] = max((P[j] - P[i]) / (j - i) + Table[j] for j in range(i + 1, N - (k - 1) + 1))

        return Table[0]
