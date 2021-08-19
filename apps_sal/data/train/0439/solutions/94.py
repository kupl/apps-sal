class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        if n == 1:
            return 1
        dp = [1 for _ in range(n)]
        dp[1] = 2 if A[0] != A[1] else 1
        maxTurb = dp[1]
        wasGreater = A[0] > A[1]
        for i in range(1, n):
            if A[i - 1] > A[i] and (not wasGreater):
                wasGreater = True
                dp[i] += dp[i - 1]
            elif A[i - 1] < A[i] and wasGreater:
                wasGreater = False
                dp[i] += dp[i - 1]
            else:
                dp[i] = 2 if A[i] != A[i - 1] else 1
            maxTurb = max(maxTurb, dp[i])
        return maxTurb
