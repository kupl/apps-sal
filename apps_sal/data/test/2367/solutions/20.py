import math
import time

DIV_VALUE = 10**9 + 7


def calcModOfPow(a, n, p):
    btm = a
    ans = 1
    while n != 0:
        # print('btm: {}'.format(btm))
        if n & 1:
            ans = (ans * btm) % p
            # print('ans: {}'.format(ans))
        n = n >> 1
        btm = (btm**2) % p
        # print(n)

    return ans


def calcModOfInv(a, p):
    b = p
    x = 1
    y = 0
    while b:
        div = a // b
        a -= div * b
        [a, b] = [b, a]
        x -= div * y
        [x, y] = [y, x]

    x %= p
    if x < 0:
        x += p

    return x


class FirstHalf:
    def __init__(self, H, W, A, B):
        self.H = H
        self.W = W
        self.A = A
        self.B = B
        self.k = 0
        self.div = 0
        self.sup = 0
        self.numOfCases = 1

    def getNumOfCases(self):
        if self.k != 0:
            self.numOfCases = self.numOfCases * (
                (self.B + self.k - 1)
            ) * (
                calcModOfInv(self.k, DIV_VALUE)
            ) % DIV_VALUE
        self.k += 1
        # print('----- k == {} -----'.format(self.k))
        # print(self.numOfCases)
        # self.numOfCases %= DIV_VALUE
        return self.numOfCases
        # return self.numOfCases % DIV_VALUE


class SecondHalf:
    def __init__(self, H, W, A, B):
        self.H = H
        self.W = W
        self.A = A
        self.B = B
        self.k = 0
        self.div = 0
        self.numOfCases = 1
        totalval = self.H + self.W - self.B - 2
        loopval = self.H - 1 if self.H < self.W - self.B else self.W - self.B - 1
        for top in range(totalval, totalval - loopval, -1):
            self.numOfCases *= top
            self.numOfCases %= DIV_VALUE
        for bottom in range(loopval, 0, -1):
            self.numOfCases *= calcModOfInv(bottom, DIV_VALUE)
            self.numOfCases %= DIV_VALUE

        # self.numOfCases = (
        #     math.factorial(self.H + self.W - self.B - 2)
        # ) // (
        #     math.factorial(self.W - self.B - 1)
        # ) // (
        #     math.factorial(self.H - 1)
        # )

    def getNumOfCases(self):
        if self.k != 0:
            self.numOfCases = self.numOfCases * (
                self.H - self.k
            ) * (
                calcModOfInv(
                    self.H + self.W - self.B - self.k - 1,
                    DIV_VALUE
                )
            ) % DIV_VALUE
        self.k += 1
        # print(self.numOfCases)
        # self.numOfCases %= DIV_VALUE
        return self.numOfCases
        # return self.numOfCases % DIV_VALUE


def __starting_point():
    [H, W, A, B] = [int(ipt) for ipt in input().split()]

    start = time.time()
    fstHlf = FirstHalf(H, W, A, B)
    sndHlf = SecondHalf(H, W, A, B)
    totalCases = 0

    mid = time.time()
    # print('mid: {}'.format(mid - start))
    for _ in range(H - A):
        totalCases += (
            fstHlf.getNumOfCases() * sndHlf.getNumOfCases()
        )
        totalCases %= DIV_VALUE

    end = time.time()
    # print('end: {}'.format(end - mid))
    print(totalCases)

    #print('{} {} {} {}'.format(H, W, A, B))
    # print(DIV_VALUE)

    # for i in range(12):
    #     print('inv: {}'.format(calcModOfInv(i+1, 13)))


__starting_point()
