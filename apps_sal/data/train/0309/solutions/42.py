class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        for _ in range(len(A)):
            dp.append({})
        max_ = 0
        dp[0][0] = 1
        for i in range(1, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                if dp[i][diff] > max_:
                    max_ = dp[i][diff]
        return max_
