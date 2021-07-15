class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2] * n for i in range(n)]
        index = [-1] * 501
        res = 2
        for i in range(n):
            for j in range(i+1, n):
                first = 2 * A[i] - A[j]
                if first < 0 or first >= 500 or index[first] == -1:
                    continue
                dp[i][j] = dp[index[first]][i] + 1
                res = max(res, dp[i][j])
            index[A[i]] = i
        return res
