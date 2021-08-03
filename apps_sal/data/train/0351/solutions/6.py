class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            res += 1
        return res + X - Y
