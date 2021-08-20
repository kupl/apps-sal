class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:
        m = 1
        n = 1
        while m * p != n * q:
            n += 1
            m = n * q // p
        if n % 2 == 0:
            return 2
        if n % 2 == 1:
            if m % 2 == 1:
                return 1
            else:
                return 0
