class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        P = [None] * (n + 1)
        P[2] = 1 / n
        for i in range(3, n + 1):
            P[i] = P[i - 1] * (1 + 1 / (n - i + 2))
        return P[n]
