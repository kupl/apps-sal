class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ans = 0
        for (i, n) in enumerate(A):
            for j in range(i):
                diff = A[j] - A[i]
                if (diff, j) not in dp:
                    dp[diff, i] = 2
                else:
                    dp[diff, i] = dp[diff, j] + 1
                ans = max(ans, dp[diff, i])
        return ans
