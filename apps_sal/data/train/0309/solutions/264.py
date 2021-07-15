class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{}]
        max_length = 1
        for i in range(1, len(A)):
            dp.append({})
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                max_length = max(max_length, dp[i][diff])

        return max_length
