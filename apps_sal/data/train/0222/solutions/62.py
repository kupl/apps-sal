class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        res = 0
        d = {x: i for (i, x) in enumerate(A)}
        n = len(A)
        dp = [[2 for j in range(n)] for i in range(n)]
        for i in range(2, n):
            for j in range(i):
                z = A[i]
                x = A[j]
                y = z - x
                k = d.get(y, -1)
                if x < y and k != -1:
                    dp[i][k] = 1 + dp[k][j]
                    res = max(res, dp[i][k])
        if res > 2:
            return res
        return 0
