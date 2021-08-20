class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        for i in range(n):
            for j in range(i + 1, n):
                dif = A[j] - A[i]
                if (i, dif) in dp:
                    dp[j, dif] = dp[i, dif] + 1
                else:
                    dp[j, dif] = 2
        return max(dp.values())
