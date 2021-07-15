class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        for _ in range(len(A)):
            dp.append({})
        max_ = 0
        for i in range(len(A)):
            for j in range(0, i):
                if i == 0:
                    dp[i][0] == 1
                else:
                    diff = A[i] - A[j]
                    if diff in dp[j]:
                        dp[i][diff] = dp[j][diff] + 1
                    else:
                        dp[i][diff] = 2
                    if dp[i][diff] > max_:
                        max_ = dp[i][diff]
        return max_
