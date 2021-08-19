class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        for i in range(1, n):
            for j in range(i):
                dif = A[i] - A[j]
                if (j, dif) in dp:
                    dp[i, dif] = dp[j, dif] + 1
                else:
                    dp[i, dif] = 2
        return max(dp.values())
