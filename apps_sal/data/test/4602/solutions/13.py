n = int(input())
k = int(input())
xn = list(map(int, input().split()))


class Solution:

    def __init__(self, n, k, xn):
        self.n = n
        self.k = k
        self.xn = xn

    @staticmethod
    def printout():
        print(n, k, xn)

    @staticmethod
    def answer():
        total = 0
        for xi in xn:
            a = abs(xi - 0)
            b = abs(xi - k)
            if a <= b:
                total += a * 2
            else:
                total += b * 2
        print(total)


conditions = Solution(n, k, xn)
conditions.answer()
