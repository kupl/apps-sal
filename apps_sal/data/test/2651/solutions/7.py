import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


class mint:
    def __init__(self, x):
        self.__x = x % md

    def __str__(self):
        return str(self.__x)

    def __add__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x + other)

    def __sub__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x - other)

    def __rsub__(self, other):
        return mint(other - self.__x)

    def __mul__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x * other)

    __radd__ = __add__
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x * pow(other, md - 2, md))

    def __pow__(self, power, modulo=None):
        return mint(pow(self.__x, power, md))


md = 10**9 + 7


def main():
    n, m = MI()
    xx = LI()
    yy = LI()
    ans = mint(0)
    byj = mint(0)
    for j in range(m - 1):
        byj += (j + 1) * (m - j - 1) * (yy[j + 1] - yy[j])
    for i in range(n - 1):
        ans += (xx[i + 1] - xx[i]) * (i + 1) * (n - i - 1) * byj

    print(ans)


main()
