d = [0] * 49011


def g(n, m, k):
    t = 1000000000.0
    for i in range(1, m // 2 + 1):
        for j in range(k + 1):
            t = min(t, f(n, m - i, k - j) + f(n, i, j))
    return n * n + t


def f(n, m, k):
    if n > m:
        (n, m) = (m, n)
    k = min(k, n * m - k)
    if k == 0:
        return 0
    if k < 0:
        return 1000000000.0
    q = n + 31 * m + 961 * k
    if d[q] == 0:
        d[q] = min(g(n, m, k), g(m, n, k))
    return d[q]


for q in range(int(input())):
    (n, m, k) = map(int, input().split())
    print(f(n, m, k))
