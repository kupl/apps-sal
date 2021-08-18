class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        n = len(A)
        if n < 2:
            return n

        dp = [{} for _ in range(n)]
        ans = 1
        dp[0] = {0: 1}
        for i in range(1, n):
            for j in range(i):
                delta = A[i] - A[j]
                if delta in list(dp[j].keys()):
                    dp[i][delta] = dp[j][delta] + 1
                else:
                    dp[i][delta] = 2
                ans = max(ans, dp[i][delta])

        return ans
