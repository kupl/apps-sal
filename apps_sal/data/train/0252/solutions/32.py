class Solution:
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            left = i- x
            right = i+x
            for j in range(max(left+1, 0), min(right, n) + 1):
                dp[j] = min(dp[j], dp[max(0, left)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
