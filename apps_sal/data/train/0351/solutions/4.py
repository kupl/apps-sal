class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X:
            return X - Y
        count = 0
        while Y > X:
            if Y % 2 == 0:
                Y = Y / 2
                count += 1
            else:
                Y += 1
                count += 1
        return int(count + X - Y)
