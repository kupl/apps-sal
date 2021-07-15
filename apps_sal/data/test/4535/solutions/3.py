class Solution:
    def hammingWeight(self, n: int) -> int:
        
        onebits = 0
        while n > 0:
            if n & 1 == 1:
                onebits += 1
            n = n >> 1
        return onebits
