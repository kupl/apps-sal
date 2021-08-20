class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:
        cnt = 0
        while Y > X:
            cnt += 1
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
        return cnt + X - Y
