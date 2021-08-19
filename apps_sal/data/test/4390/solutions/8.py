import sys


def RI():
    return [int(x) for x in sys.stdin.readline().split()]


def ri():
    return sys.stdin.readline().strip()


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


INF = 10 ** 18
MOD = 10 ** 9 + 7
for i in range(int(ri())):
    (a, b) = RI()
    temp = a % b
    if temp == 0:
        print(0)
    else:
        print(b - temp)
