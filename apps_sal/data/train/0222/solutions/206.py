class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # https://blog.csdn.net/fuxuemingzhu/article/details/82715323
        n = len(A)
        m = dict()
        for i, a in enumerate(A):
            m[a] = i
        res = 0
        # dp[i][j] := max len of seq ends with A[i], A[j]
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
