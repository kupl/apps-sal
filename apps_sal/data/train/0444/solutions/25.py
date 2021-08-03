class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        p = [None, 1., 0.5]
        for i in range(2, n):
            prob = (i * p[i] + p[i]) / (i + 1)
            p.append(prob)
        return p[n]
