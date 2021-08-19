class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1

        # let P(k) be the probability that the k-th person loses his seat
        # it can be shown that: P(k) = P(k-1)(1 + 1/(n-k+2))
        P = [None] * (n + 1)
        P[2] = 1 / n

        for i in range(3, n + 1):
            P[i] = P[i - 1] * (1 + 1 / (n - i + 2))

        return P[n]
