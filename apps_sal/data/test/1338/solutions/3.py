arc = []


def sv(a, b, c, n, v):
    if n < c // 2:
        arc[a] = v
        if b - a > 1:
            sv(a + 1, b, c // 2, n, v + 1)
    else:
        arc[b - 1] = v
        if b - a > 1:
            sv(a, b - 1, c // 2, n - c // 2, v + 1)


(n, m) = list(map(int, input().split()))
arc = [0] * n
ssc = 1 << n - 1
sv(0, n, ssc, m - 1, 1)
print(' '.join(map(str, arc)))
