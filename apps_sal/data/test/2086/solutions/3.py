R = lambda: map(int, input().split())

n = int(input())
a = list(R())
s, f = R()

d = f - s


def solve(a, d, n, s):
    if (n < d + 1):
        return s

    t = 0
    for i in range(0, d):
        t += a[i]

    m = t
    res = s
    for i in range(1, n):
        t += a[(i + d - 1) % n] - a[i - 1]
        if t > m:
            m = t
            res = gr(i, s, n)
        elif t == m:
            res = min(res, gr(i, s, n))

    return res


def gr(i, s, n):
    res = (s - i) % n
    if (res <= 0):
        return n - res
    return res


print(solve(a, d, n, s))
