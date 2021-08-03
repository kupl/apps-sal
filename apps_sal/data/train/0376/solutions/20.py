class Solution:
    def minScoreTriangulation_v2(self, A: List[int]) -> int:
        length = len(A)
        DP = [[float('inf')] * length for _ in range(len(A))]
        for e in range(2, length):
            for i in range(length - e):
                j = i + e
                for k in range(i + 1, j):
                    left_point = DP[i][k] if k >= i + 2 else 0
                    right_point = DP[k][j] if j >= k + 2 else 0
                    DP[i][j] = min(DP[i][j], left_point + A[i] * A[j] * A[k] + right_point)
        return DP[0][len(A) - 1]

    def minScoreTriangulation(self, A: List[int]) -> int:
        length = len(A)
        memo = [[float('inf')] * length for _ in range(len(A))]

        def memo_dp(start, end):
            if end - start < 2:
                return 0
            if end - start == 2:
                memo[start][end] = A[start] * A[start + 1] * A[end]
                return memo[start][end]
            if memo[start][end] != float('inf'):
                return memo[start][end]

            val = memo[start][end]
            for i in range(start + 1, end):
                val = min(val, A[start] * A[i] * A[end] + memo_dp(start, i) + memo_dp(i, end))
            memo[start][end] = val
            return memo[start][end]

        memo_dp(0, length - 1)
        return memo[0][length - 1]
