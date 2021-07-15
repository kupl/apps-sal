class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        m = int(sqrt(2*N)+1)
        for i in range(1,m):
            N -= i
            if N % i == 0:
                res += 1
        return res
