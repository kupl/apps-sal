import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n = mint()
    print((n + 1) * 3 + 1)
    for i in range(n + 1):
        print(i, i)
        print(1 + i, i)
        print(i, 1 + i)
    print(n + 1, n + 1)


# for i in range(mint()):
solve()
