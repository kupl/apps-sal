n, m, k = map(int, input().split())
n, m = min(n, m), max(n, m)


def p(i, j):
    return (n // (i + 1)) * (m // (j + 1))


if k < n:
    print(max(p(k, 0), p(0, k)))
elif k < m:
    print(p(0, k))
elif k <= n + m - 2:
    print(p(k - (m - 1), m - 1))
else:
    print(-1)
