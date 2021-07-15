class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        n = 1
        
        while N > self.math(n):
            if (N-self.math(n)) % n == 0:
                res += 1
            n += 1
        
        return res
    
    def math(self, n):
        return (n-1)*n//2
