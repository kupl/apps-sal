import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


def solve1(a):
    n = len(a)


def solve():
    n = mint()
    a = list(mints())
    if n == 1:
        print(a[0])
        return
    a += a
    b = [0] * (2 * n)
    b[0] = a[0]
    b[1] = a[1]
    for i in range(2, len(b)):
        b[i] = b[i - 2] + a[i]
    r = min(b[n - 3], b[n - 3 + 1])
    for j in range(n - 3 + 2, len(b)):
        r = min(r, b[j] - b[j - (n - 3) - 2])
    print(sum(a) // 2 - r)


solve()
