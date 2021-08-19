class Solution:

    def soupServings(self, N: int) -> float:
        if N > 5000:
            return 1
        dp = [[-1 for i in range(N + 1)] for j in range(N + 1)]
        return self.helper(N, N, dp)

    def helper(self, A, B, dp):
        if A <= 0 and B <= 0:
            return 0.5
        if A <= 0:
            return 1
        if B <= 0:
            return 0
        if dp[A][B] != -1:
            return dp[A][B]
        dp[A][B] = (self.helper(A - 100, B - 0, dp) + self.helper(A - 75, B - 25, dp) + self.helper(A - 50, B - 50, dp) + self.helper(A - 25, B - 75, dp)) * 0.25
        return dp[A][B]
