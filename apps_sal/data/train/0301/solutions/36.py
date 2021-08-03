class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        dp = [0] * (N + 1)
        res = 0
        for i in range(1, M + 1):
            dp2 = [0] * (N + 1)
            for j in range(1, N + 1):
                if A[i - 1] == B[j - 1]:
                    dp2[j] = dp[j - 1] + 1
                else:
                    dp2[j] = max(dp[j], dp2[j - 1])

            dp = dp2
            res = max(res, max(dp))

        return res
