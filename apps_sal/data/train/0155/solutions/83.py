class Solution:

    def maxJumps(self, A: List[int], d: int) -> int:
        n = len(A)
        dp = [1] * n
        for (a, i) in sorted(([a, i] for (i, a) in enumerate(A))):
            j = i - 1
            while j >= 0 and A[j] < A[i] and (i - j <= d):
                dp[i] = max(dp[i], dp[j] + 1)
                j -= 1
            j = i + 1
            while j < n and A[j] < A[i] and (j - i <= d):
                dp[i] = max(dp[i], dp[j] + 1)
                j += 1
        return max(dp)
