#!/usr/bin/env python3
def binsearch(p, l, r):  # (l,r], return the smallest n which p holds
    while l + 1 != r:
        m = (l + r) // 2
        if p(m):
            r = m
        else:
            l = m
    return r


n = int(input())
if n == 0:
    print(0, 0)
else:
    i = binsearch(lambda i: n <= 3 * i * (i + 1), 0, 10**18)
    acc = 3 * (i - 1) * i
    j = binsearch(lambda j: n <= acc + i * (j + 1), -1, 6)
    k = n - acc - i * j - 1
    dy = [0, 2, 2, 0, -2, -2]
    dx = [2, 1, -1, -2, -1, 1]
    y = dy[(j + 1) % 6] + dy[j] * (i - 1) + dy[(j + 2) % 6] * k
    x = dx[(j + 1) % 6] + dx[j] * (i - 1) + dx[(j + 2) % 6] * k
    print(x, y)
