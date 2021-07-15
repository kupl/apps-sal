class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        res = 1.0
        t = 1.0
        
        for i in range(2, n + 1):
            res = (1 / i) * t
            t += res
        
        return res
