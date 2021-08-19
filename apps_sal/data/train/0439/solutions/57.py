class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        dp = [0 for _ in range(len(A))]
        dp[0] = 1
        dp[1] = 2 if A[1] != A[0] else 1
        for i in range(2, len(A)):
            if A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]:
                dp[i] = dp[i - 1] + 1
            elif A[i] == A[i - 1]:
                dp[i] = 1
            else:
                dp[i] = 2
        print(dp)
        return max(dp)
