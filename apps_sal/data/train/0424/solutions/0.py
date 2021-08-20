class Solution:

    def largestOverlap(self, A, B) -> int:
        leng = len(A[0])
        a = 0
        b = 0
        for i in range(0, leng * leng):
            row = int(i % leng)
            col = int(i / leng)
            a = (a << 1) + A[col][row]
            b = (b << 1) + B[col][row]
        maxsum = 0
        for i in range(-leng + 1, leng):
            if i < 0:
                mask = ('0' * abs(i) + '1' * (leng - abs(i))) * leng
                bp = (b & int(mask, 2)) << abs(i)
            elif i > 0:
                mask = ('1' * (leng - abs(i)) + '0' * abs(i)) * leng
                bp = (b & int(mask, 2)) >> abs(i)
            else:
                bp = b
            for j in range(-leng + 1, leng):
                if j < 0:
                    bpp = bp >> leng * abs(j)
                elif j > 0:
                    bpp = bp << leng * abs(j) & 2 ** (leng * leng) - 1
                else:
                    bpp = bp
                maxsum = max(maxsum, bin(a & bpp).count('1'))
        return maxsum
