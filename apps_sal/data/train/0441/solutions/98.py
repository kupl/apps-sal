class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        maxLen = int(((1+8*N)**0.5-1)/2)
        nWays = 1           # at least 1 way: N = N
        for n in range(2, maxLen+1):
            nWays += (2*N+n-n**2)%(2*n) == 0
        return nWays
        

