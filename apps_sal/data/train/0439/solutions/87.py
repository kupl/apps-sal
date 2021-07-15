class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                dp[i] = 1
            elif A[i] < A[i - 1]:
                dp[i] = -1
        res = 0
        for i in range(1, n):
            if dp[i] == 0:
                curr = 0
                continue
            if dp[i] + dp[i - 1] != 0:
                curr = 1
            else:
                curr += 1
            res = max(res, curr)
        return res + 1

