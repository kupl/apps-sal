import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    (n, m) = mints()
    a = list(mints())
    a.sort()
    rr = [0] * n
    c = [0] * m
    ss = 0
    for i in range(1, n + 1):
        ss += a[i - 1]
        ss += c[(i - 1) % m]
        c[(i - 1) % m] += a[i - 1]
        rr[i - 1] = ss
    print(' '.join(map(str, rr)))


solve()
