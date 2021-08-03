class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for i in A]
        if len(A) <= 2:
            return len(A)
        ans = 0

        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = max(2, dp[j][diff] + 1)

                else:
                    dp[i][diff] = 2

                ans = max(ans, dp[i][diff])
        return ans
