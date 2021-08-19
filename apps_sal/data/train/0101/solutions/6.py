import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    (a, b, c, r) = mints()
    if a > b:
        (a, b) = (b, a)
    return b - a - max(min(c + r, b) - max(c - r, a), 0)


for i in range(mint()):
    print(solve())
