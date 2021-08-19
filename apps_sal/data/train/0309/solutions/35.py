class Solution(object):

    def longestArithSeqLength(self, A):
        if not A:
            return None
        dp = [{} for i in range(0, len(A))]
        for i in range(len(A)):
            if i == 0:
                dp[i][0] = 1
            else:
                for j in range(0, i):
                    diff = A[i] - A[j]
                    if diff in dp[j]:
                        dp[i][diff] = dp[j][diff] + 1
                    else:
                        dp[i][diff] = 2
        mx = 2
        for j in range(len(A)):
            for i in dp[j]:
                mx = max(dp[j][i], mx)
        return mx
