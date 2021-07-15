class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 1
        
        # Remove all even factors
        while N % 2 == 0:
            N //= 2
        
        # Count all odd factors
        idx = 3        
        while idx * idx <= N:
            count = 0
            
            # found an odd factor
            while N % idx == 0:
                N //= idx
                count += 1
            
            res *= count + 1
            idx += 2
        
        return res if N == 1 else res * 2
