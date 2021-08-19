class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:
        steps = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            steps += 1
        return steps + X - Y
