class Solution:
    def baseNeg2(self, N: int) -> str:
        return str(bin((0xAAAAAAAAAAAAAAAA+N)^0xAAAAAAAAAAAAAAAA))[2:]
