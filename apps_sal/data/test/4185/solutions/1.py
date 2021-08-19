import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    (n, m) = mints()
    a = [None] * n
    for i in range(n):
        a[i] = list(mints())
    r = 0
    for j in range(m):
        c = [0] * n
        for i in range(n):
            x = a[i][j] - 1
            if x % m == j and x < n * m:
                t = (x - j) // m
                if i - t >= 0:
                    c[i - t] += 1
                else:
                    c[i - t + n] += 1
        mi = int(1000000000.0)
        for i in range(n):
            mi = min(mi, i + n - c[i])
        r += mi
    print(r)


solve()
