class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            if c & 1 == 0:
                if a & 1:
                    flips += 1
                if b & 1:
                    flips += 1
            elif a & 1 == 0 and b & 1 == 0:
                flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
