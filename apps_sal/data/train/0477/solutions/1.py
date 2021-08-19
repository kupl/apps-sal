class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        return str(k // (k & -k) >> 1 & 1 ^ (k & 1 ^ 1))

    def findKthBit_logn(self, n: int, k: int) -> str:
        (cur, flip) = (1 << n - 1, 0)
        while k > 1:
            if k & k - 1 == 0:
                return str(flip ^ 1)
            if k > cur:
                k = 2 * cur - k
                flip ^= 1
            cur >>= 1
        return str(flip)
