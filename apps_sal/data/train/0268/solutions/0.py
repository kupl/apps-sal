class Solution:
    def baseNeg2(self, N: int) -> str:

        neg = [1 << i for i in range(1, 33, 2)]
        for mask in neg:
            if N & mask:
                N += mask * 2
        return bin(N)[2:]
