#!/usr/bin/env python3

MOD = None

def matunit(n):
    return [ [ int(y == x) for x in range(n) ] for y in range(n) ]

def matadd(a, b):
    assert len(a) == len(b)
    assert len(a[0]) == len(b[0])
    h = len(a)
    w = len(a[0])
    c = [ [ a[y][x] + b[y][x] for x in range(w) ] for y in range(h) ]
    return c

def matmul(a, b):
    assert len(a[0]) == len(b)
    h = len(a)
    k = len(b)
    w = len(b[0])
    c = [ [ 0 for _ in range(w) ] for _ in range(h) ]
    for y in range(h):
        for z in range(k):
            for x in range(w):
                c[y][x] += a[y][z] * b[z][x]
    for y in range(h):
        for x in range(w):
            c[y][x] %= MOD
    return c

def matpow(a, k):
    assert len(a) == len(a[0])
    n = len(a)
    b = matunit(n)
    while k:
        if k & 1:
            b = matmul(b, a)
        a = matmul(a, a)
        k >>= 1
    return b

def binsearch(l, r, pred): # [l, r)
    assert l < r
    l -= 1
    while r - l > 1:
        m = (l + r) // 2
        if pred(m):
            r = m
        else:
            l = m
    return r

def main():
    l, a, b, m = list(map(int, input().split()))

    nonlocal MOD
    MOD = m

    x = [ [ 0 ], [ a ], [ 1 ] ]  # (answer, s_i, 1)
    DIGITS = 20
    d = [ binsearch(0, l, lambda i: len(str(a + b * i)) >= d) for d in range(DIGITS) ]
    for i in range(DIGITS - 1):
        l = d[i]
        r = d[i + 1]
        f = [ [ 10 ** i, 1, 0 ], [ 0, 1, b ], [ 0, 0, 1 ] ]
        x = matmul(matpow(f, r - l), x)
    print((x[0][0] % m))


def __starting_point():
    main()

__starting_point()
