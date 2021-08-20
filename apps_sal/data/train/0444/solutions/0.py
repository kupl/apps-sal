class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 / min(n, 2.0)
