class Solution:

    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:]
        z = '0' * (32 - len(a)) + a
        t = z[::-1]
        return int(t, 2)
