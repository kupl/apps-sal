class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        current = 1
        next_addition = 10
        num_digits = 1
        while current % K != 0:
            current += next_addition
            next_addition *= 10
            num_digits += 1
            
        return num_digits
