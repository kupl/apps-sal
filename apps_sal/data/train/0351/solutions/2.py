class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:
        cnt = 0
        while Y > X:
            if Y % 2 != 0:
                Y = Y + 1
            else:
                Y = Y // 2
            cnt += 1
        if X > Y:
            cnt += int(X - Y)
        return cnt
