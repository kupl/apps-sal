class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:

        if n == 1:
            return 1

        s = 0
        for i in range(1, n - 1):
            s += 0.5 / n

        return 1 / n + s
