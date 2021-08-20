class Solution:

    def minScoreTriangulation(self, A: List[int]) -> int:
        memo = [[0] * len(A) for _ in range(len(A))]
        for i in reversed(range(len(A))):
            for j in range(i + 2, len(A)):
                memo[i][j] = min((memo[i][k] + A[i] * A[k] * A[j] + memo[k][j] for k in range(i + 1, j)))
        return memo[0][-1]
