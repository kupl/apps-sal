class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        dp = {}
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2
                ans = max(ans, dp[i, d])
        return ans
