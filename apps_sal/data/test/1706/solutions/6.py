import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    s = minp()
    n = len(s)
    print(3)
    print('R', n - 1)
    print('L', n)
    print('L', 2)


solve()
