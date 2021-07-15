class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        D = [0]*n
        D[0] = 1.0
        for i in range(1,n):
            D[i] = 1/(i+1) + (i-1)/(i+1)*D[i-1]
        return D[-1]
