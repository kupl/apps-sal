class ReallyBigNumbers:

    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.binarySearch()

    def binarySearch(self):
        l = self.s
        h = 10000000000000000000
        while(l < h):
            mid = (h + l) // 2
            if self.isReallyBig(mid):
                h = mid
            else:
                l = mid + 1
        self.x = int(l)

    def isReallyBig(self, v):
        cp = v
        add = 0
        while v > 0:
            add += v % 10
            v //= 10
        return (cp - add) >= self.s

    def show(self):
        if self.x <= self.n:
            print(str(self.n - self.x + 1))
        else:
            print(0)


n, s = list(map(int, input().split()))
rbg = ReallyBigNumbers(n, s)
rbg.show()
