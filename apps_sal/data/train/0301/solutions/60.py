class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a = len(A)
        dp = [0] * len_a
        for n in B:
            prev = dp[0]
            if n == A[0]:
                dp[0] = 1
            for idx in range(1, len_a):
                if n == A[idx]:
                    prev, dp[idx] = dp[idx], prev + 1
                else:
                    prev, dp[idx] = dp[idx], max(dp[idx - 1], dp[idx])

        return dp[-1]
