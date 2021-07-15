class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        res = 1
        n=N
        for i in range(2, math.floor((1 + (1+8*n)**0.5) / 2)):
            
            if ((n/i) - (i-1)/2).is_integer():
                res += 1

        return res
