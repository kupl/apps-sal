class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i = 1
        res = 0
        while N > i*(i-1)//2:
            if (N - i*(i-1)//2) % i == 0:
                res += 1
            i += 1
        return res
            
            
# N = k + k+1 + ... k+i-1
# N = k*i + (0+i-1)*i/2
# N - i*(i-1)/2 = k*i

