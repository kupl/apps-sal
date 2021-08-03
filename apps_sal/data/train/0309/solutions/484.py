class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        maximum = 1

        for i in range(len(A)):
            d = {}
            dp.append(d)
            for j in range(i):
                dp[i][A[i] - A[j]] = dp[j][A[i] - A[j]] = 0

        for i in range(len(A)):
            d = {}
            dp.append({})
            for j in range(i):
                diff = A[i] - A[j]

                dp[i][diff] = dp[j][diff] + 1
                maximum = max(maximum, dp[i][diff])

        return maximum + 1
