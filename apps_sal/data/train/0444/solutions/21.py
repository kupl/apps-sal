class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        good = 0
        left = n
        uncenrtain = 1
        while left >= 2:
            good += uncenrtain / left
            uncenrtain = uncenrtain * (left - 2) / left
            left -= 1
        return good
