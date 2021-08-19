class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        mem = {}
        mem[1] = 1.0
        mem[2] = 0.5
        for i in range(3, n + 1):
            mem[i] = mem[i - 1]
        return mem[n]
