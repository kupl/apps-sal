class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indexes = {A[i]: i for i in range(len(A))}
        dp = [[2 for i in range(len(A))] for j in range(len(A))]
        z = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                idx = indexes.get(A[i] + A[j], -1)
                if idx == -1:
                    continue
                else:
                    dp[i][idx] = dp[j][i] + 1
            z = max(max(dp[i]), z)
        if z < 3:
            return 0
        return z
