class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2 for _ in range(n)] for _ in range(n)]
        indMap = {x: i for (i, x) in enumerate(A)}
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if diff in indMap and indMap[diff] < i:
                    k = indMap[diff]
                    dp[i][j] = max(dp[i][j], 1 + dp[k][i])
        res = 0
        for row in dp:
            for v in row:
                if v > 2:
                    res = max(res, v)
        return res
