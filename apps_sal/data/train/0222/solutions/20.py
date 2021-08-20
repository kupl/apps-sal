class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        v2i = {v: i for (i, v) in enumerate(A)}
        dp = [[2] * n for _ in range(0, n)]
        ret = 0
        for n3 in range(2, n):
            for n1 in range(0, n3 - 1):
                diff = A[n3] - A[n1]
                if diff < A[n1]:
                    continue
                n2 = v2i.get(diff, -1)
                if n2 != -1:
                    length = dp[n1][n2] + 1
                    if length > dp[n2][n3]:
                        dp[n2][n3] = length
                        ret = max(ret, length)
        return ret
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
