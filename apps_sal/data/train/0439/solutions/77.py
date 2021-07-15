class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        dp = [0] * len(A)
        for i in range(1, len(A)):
            if A[i] == A[i - 1]: continue
            dp[i] = 1 if A[i] > A[i - 1] else -1
        res = 0
        for i in range(1, len(A)):
            if dp[i] == 0:
                curr = 0
                continue
            curr = curr + 1 if dp[i] + dp[i - 1] == 0 else 1
            res = max(res, curr)
        return res + 1

