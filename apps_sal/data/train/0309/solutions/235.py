class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        n = len(A)
        ans = 0

        for _ in range(n):
            dp.append({})

        for i in range(n):
            for j in range(0, i):
                if i == 0:
                    dp[i][0] = 1
                else:
                    diff = A[i] - A[j]

                    if diff in dp[j]:
                        dp[i][diff] = dp[j][diff] + 1
                    else:
                        dp[i][diff] = 2

                    ans = max(ans, dp[i][diff])

        return ans
