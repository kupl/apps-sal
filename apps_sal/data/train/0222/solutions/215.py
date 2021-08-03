class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        m = {}
        for i in range(len(A)):
            m[A[i]] = i
        n = len(A)
        dp = [[2] * n for _ in range(n)]
        res = 0
        for j in range(n):
            for k in range(j + 1, n):
                ai = A[k] - A[j]
                if ai >= A[j]:
                    break
                if ai not in m:
                    continue
                i = m[ai]
                dp[j][k] = dp[i][j] + 1
                res = max(res, dp[j][k])
        return res
