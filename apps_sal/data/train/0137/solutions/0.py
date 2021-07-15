class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        s = 0
        m = n
        while m:
            s += m & 1
            m >>= 1

        k = 1
        while s:
            s -= bool(n & k)
            n ^= (s & 1) and k
            k <<= 1

        return n
