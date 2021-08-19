class Solution:

    def baseNeg2(self, N: int) -> str:
        return str(bin(12297829382473034410 + N ^ 12297829382473034410))[2:]
