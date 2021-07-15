class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        def canwrite(N, n):
            x = (N -  n * (n+1) / 2)
            return  x >=0 and x% n == 0
        res = 0
        for i in range(1,int(sqrt(2*N)+1)):
            if canwrite(N,i):
                res += 1
        return res
