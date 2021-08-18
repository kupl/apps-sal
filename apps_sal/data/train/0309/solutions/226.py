class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [dict() for _ in range(n)]
        max_len = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_len = max(max_len, dp[i][diff])
        return max_len
