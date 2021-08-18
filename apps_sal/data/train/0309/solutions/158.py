class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        ans = 2

        if n < 2:
            return n
        h = max(A)
        dp = [{} for j in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                if d in dp[j]:

                    dp[i][d] = dp[j][d] + 1
                else:
                    dp[i][d] = 2
                ans = max(ans, dp[i][d])

        return ans
