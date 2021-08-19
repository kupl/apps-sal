class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if (i, diff) not in dp:
                    dp[j, diff] = 2
                else:
                    dp[j, diff] = dp[i, diff] + 1
                ans = max(ans, dp[j, diff])
        return ans
