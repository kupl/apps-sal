class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        n = 1

        while (n * q % p):
            n += 1

        m = n * q // p

        if n & 1 == 0:
            return 2
        elif m & 1 == 0:
            return 0
        else:
            return 1
