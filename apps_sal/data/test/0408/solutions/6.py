import sys


def read(t=int):
    return list(map(t, sys.stdin.readline().split()))


array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0
(n, m) = read()


def smart(n, m):
    best = 0
    for a in range(min(n, m) + 1):
        b = min((m - a) // 2, n - 2 * a)
        best = max(best, a + b)
    return best


def brute(n, m):
    best = 0
    for a in range(max(n, m) + 1):
        for b in range(max(n, m) + 1):
            if 2 * a + b <= m and 2 * b + a <= n:
                best = max(best, a + b)
    return best


print(smart(n, m))
