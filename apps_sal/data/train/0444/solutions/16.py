class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        cur = 1
        for i in range(2, n+1):
            cur = 1/i + (i-2)/i*cur
        return cur
