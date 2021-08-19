class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        total = 0
        n = len(A)
        if n <= 2:
            return sum(A) - 1
        a_1 = [a + i for (i, a) in enumerate(A)]
        a_2 = [a - j for (j, a) in enumerate(A)]
        dp2 = [a for a in a_2]
        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 1], a_2[i + 1])
        dp1 = [a for a in a_1]
        dp1[0] += dp2[0]
        for i in range(1, n - 1):
            dp1[i] = max(a_1[i] + dp2[i], dp1[i - 1])
        return dp1[-2]
