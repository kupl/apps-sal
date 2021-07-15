class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ret = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2
            ret += 1
        return ret + X - Y
