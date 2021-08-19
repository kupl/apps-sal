class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        max_len = 0
        # index_of_array: {diff: curr_max_len}
        dp = [{} for _ in range(len(A))]

        for i in range(1, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]

                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2

                max_len = max(max_len, dp[i][diff])

        return max_len
