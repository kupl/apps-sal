def g(a, b):
    cur = 1
    res = 0
    ze = 0
    while cur <= b:
        if b & cur:
            b ^= cur
            if a & b == 0:
                res += (1 << ze)
        if a & cur == 0:
            ze = ze + 1
        cur <<= 1
    return res


def f(a, b):
    res = 0
    if a == b:
        return 0
    if a == 0:
        return 2 * b - 1 + f(1, b)
    if a & 1:
        res = res + 2 * (g(a, b) - g(a, a))
        a = a + 1
    if b & 1:
        res = res + 2 * (g(b - 1, b) - g(b - 1, a))
    return 3 * f(a >> 1, b >> 1) + res


t = int(input())

while t > 0:
    t = t - 1
    l, r = map(int, input().split())
    print(f(l, r + 1))
