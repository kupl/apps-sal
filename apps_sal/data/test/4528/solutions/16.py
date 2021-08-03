import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    a, b = mints()
    print(24 * 60 - a * 60 - b)


for i in range(mint()):
    solve()
