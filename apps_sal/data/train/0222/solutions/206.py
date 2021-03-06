class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        m = dict()
        for (i, a) in enumerate(A):
            m[a] = i
        res = 0
        dp = [[2 for i in range(n)] for j in range(n)]
        for j in range(n):
            for k in range(j + 1, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                if a_i in m:
                    i = m[a_i]
                    dp[j][k] = dp[i][j] + 1
                    res = max(res, dp[j][k])
        return res
