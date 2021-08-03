class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:

        count = 0

        while Y != X:
            if Y < X:
                count += X - Y
                Y = X
            elif Y % 2 == 0:
                Y //= 2
                count += 1
            else:
                Y += 1
                count += 1
        return count
