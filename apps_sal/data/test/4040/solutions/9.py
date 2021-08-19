import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    (n, m, d) = mints()
    a = list(mints())
    b = [0] * m
    s = sum(a)
    p = 0
    for i in range(m):
        b[i] = p + d
        p = p + d + a[i] - 1
    if b[-1] + a[-1] - 1 + d < n + 1:
        print('NO')
        return
    p = n + 1
    c = [0] * n
    for i in range(m - 1, -1, -1):
        if b[i] + a[i] - 1 >= p:
            b[i] = p - a[i]
        p = b[i]
        for j in range(b[i], b[i] + a[i]):
            c[j - 1] = i + 1
    print('YES')
    print(*c)


solve()
