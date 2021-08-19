class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            ai = a & mask
            bi = b & mask
            ci = c & mask
            if ci == 0:
                if ai and bi:
                    res += 2
                elif ai or bi:
                    res += 1
            elif not ai and (not bi):
                res += 1
        return res
