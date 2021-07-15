class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = [A[0][:], [0 for _ in A[0]]]
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                dp[i & 1][j] = min([dp[(i - 1) & 1][j + k] + A[i][j] for k in (-1, 0, 1) if 0 <= j + k < len(A[i])])
        return min(dp[(len(A) - 1) & 1])

