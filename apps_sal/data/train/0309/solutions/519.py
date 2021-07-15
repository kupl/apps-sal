class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n == 2:
            return n
        dp = [{} for i in range(n)]
        max_len = 0
        for i in range(1,n):
            for j in range(i):
                diff = A[i]-A[j]
                if diff in dp[j]:
                    dp[i][diff] = max(2, 1+dp[j][diff])
                else:
                    dp[i][diff] = 2
                max_len = max(max_len, dp[i][diff])
        return max_len
