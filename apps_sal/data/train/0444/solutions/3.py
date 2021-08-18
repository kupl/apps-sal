class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        if n == 2:
            return 0.5
        return 0.5
        if n == 3:
            return (1 / 3 * 1 + 1 / 3 * 1 / 2 + 1 / 3 * 0)
        if n == 4:
            return (1 / 4 * 1 + 1 / 4 * (1 / 3 * 1 + 1 / 3 * 1 / 2 + 1 / 3 * 0) + 1 / 4 * (1 / 3 * 1 + 1 / 3 * 1 + 1 / 3 * 0) + 1 / 4 * 0)

        return (1 / n * 1 + (n - 2) / n * self.nthPersonGetsNthSeat(n - 2) + 1 / n * 0)
