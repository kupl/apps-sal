class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        if n == 2:
            return 0.5
        result = 1.0
        curr = 1.0
        for i in range(2, n + 1):
            result = 1 / i * curr
            curr += result
        return result
