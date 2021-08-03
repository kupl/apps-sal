import sys

w, m, k = map(int, input().split())


def next(n):
    a, cnt = 1, 1
    while a <= n:
        a *= 10
        cnt += 1
    return a, cnt - 1


m0 = m

while w > 0:
    M, s = next(m)
    if (M - m) * s * k >= w:
        M = (w + m * s * k) // (s * k)
        print(M - m0)
        return
    else:
        w -= (M - m) * s * k
        m = M
