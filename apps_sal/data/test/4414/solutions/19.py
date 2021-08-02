import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    a, b, n, S = mints()
    d = S // n
    r = S % n
    d = min(a, d)
    print(["NO", "YES"][S - d * n <= b])


for i in range(mint()):
    solve()
