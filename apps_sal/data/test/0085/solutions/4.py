def decomp(a):
    cnt2 = 0
    while a % 2 == 0:
        a = a // 2
        cnt2 += 1
    cnt3 = 0
    while a % 3 == 0:
        a = a // 3
        cnt3 += 1
    return a, cnt2, cnt3


def cut(a, b, d, p):
    while d > 0:
        if a % p == 0:
            a = (p - 1) * a // p
            d = d - 1
        elif b % p == 0:
            b = (p - 1) * b // p
            d = d - 1
    return a, b


a1, b1 = [int(s) for s in input().split()]
a2, b2 = [int(s) for s in input().split()]

u1, n2a1, n3a1 = decomp(a1)
v1, n2b1, n3b1 = decomp(b1)

u2, n2a2, n3a2 = decomp(a2)
v2, n2b2, n3b2 = decomp(b2)

if u1 * v1 != u2 * v2:
    print(-1)
else:
    n = n2a1 + n2b1
    m = n3a1 + n3b1
    x = n2a2 + n2b2
    y = n3a2 + n3b2

    d3 = abs(m - y)
    if m > y:
        n += d3
        a1, b1 = cut(a1, b1, d3, 3)
    else:
        x += d3
        a2, b2 = cut(a2, b2, d3, 3)
    d2 = abs(n - x)
    if n > x:
        a1, b1 = cut(a1, b1, d2, 2)
    else:
        a2, b2 = cut(a2, b2, d2, 2)

    m = d2 + d3

    print(m)
    print(a1, b1)
    print(a2, b2)
