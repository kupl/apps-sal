class Solution:

    def soupServings(self, N: int) -> float:

        def prob(A, B, dp):
            if A == 0 and B == 0:
                return 0.5
            if A == 0:
                return 1.0
            if dp[A][B] != -1.0:
                return dp[A][B]
            else:
                total_prob = 0
                total_prob += 1 / 4 * prob(max(0, A - 100), B, dp)
                if B - 25 > 0 or (A - 75 <= 0 and B - 25 <= 0):
                    total_prob += 1 / 4 * prob(max(0, A - 75), max(0, B - 25), dp)
                if B - 50 > 0 or (A - 50 <= 0 and B - 50 <= 0):
                    total_prob += 1 / 4 * prob(max(0, A - 50), max(0, B - 50), dp)
                if B - 75 > 0 or (A - 25 <= 0 and B - 75 <= 0):
                    total_prob += 1 / 4 * prob(max(0, A - 25), max(0, B - 75), dp)
                dp[A][B] = total_prob
                return dp[A][B]
        if N > 4800:
            return 1.0
        dp = [[-1.0 for i in range(N + 1)] for j in range(N + 1)]
        return prob(N, N, dp)
