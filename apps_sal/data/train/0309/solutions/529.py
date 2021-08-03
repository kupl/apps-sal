class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        minimum = min(A)
        maximum = max(A)

        length = 2 * (maximum - minimum) + 1

        dp = [[1 for i in range(length)] for j in range(len(A))]

        diff = maximum - minimum
        ans = 0
        for i in range(len(dp)):
            for j in range(i):
                dp[i][A[i] - A[j] + diff] = max(dp[i][A[i] - A[j] + diff], dp[j][A[i] - A[j] + diff] + 1)
                ans = max(ans, dp[i][A[i] - A[j] + diff])
        return ans
