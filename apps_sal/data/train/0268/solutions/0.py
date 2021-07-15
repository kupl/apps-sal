class Solution:
    def baseNeg2(self, N: int) -> str:
        # res = []
        # x = N
        # while x:
        #     res.append(x & 1)
        #     x = -(x >> 1)
        # return \"\".join(map(str, res[::-1] or [0]))
        
        neg = [1 << i for i in range(1, 33, 2)]
        for mask in neg:
            if N & mask: N += mask*2
        return bin(N)[2:]
