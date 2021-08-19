from math import factorial as fac


class Solution:

    def getProbability(self, balls: List[int]) -> float:

        def ways(nums):
            tmp = fac(sum(nums))
            for num in nums:
                tmp //= fac(num)
            return tmp

        def dist(pos, rem):
            if pos == len(balls):
                if rem == 0:
                    isValid()
                return
            for i in range(min(balls[pos], rem) + 1):
                a[pos] = i
                b[pos] = balls[pos] - i
                dist(pos + 1, rem - i)

        def isValid():
            x = y = 0
            x = sum((1 for i in a if i > 0))
            y = sum((1 for j in b if j > 0))
            if x == y:
                self.res += ways(a) * ways(b)
        total = sum(balls)
        n = len(balls)
        a = [0] * n
        b = [0] * n
        self.res = 0
        dist(0, total // 2)
        return self.res / ways(balls)
