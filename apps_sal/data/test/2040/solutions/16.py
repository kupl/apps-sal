def nd(n):
    v = 0
    while n:
        n, v = n // 10, v + 1
    return v


def sd(n):
    v = 0
    while n:
        n, v = n // 10, v + n % 10
    return v


def mina(s):
    d9 = s // 9
    return (s % 9 + 1) * 10 ** d9 - 1


def maxan(s, n):
    v = 0
    for i in range(n - 1, -1, -1):
        c = min(s, 9)
        s -= c
        v += c * 10 ** i
    return v


def minan(s, n):
    d9 = (s - 1) // 9
    return 10 ** d9 - 1 + 10 ** (n - 1) + (s - 1) % 9 * 10 ** d9


def f(s, m):
    a1 = mina(s)
    if a1 > m:
        return a1
    n = nd(m)
    if m >= maxan(s, n):
        return minan(s, n + 1)
    for i in range(n):
        if m // 10 ** i % 10 == 9:
            continue
        x = m - m % 10 ** i + 10 ** i
        sx = sd(x)
        if sx > s:
            continue
        for j in range(i + 1):
            d = x // 10 ** j % 10
            c = min(9 - d, s - sx)
            x += c * 10 ** j
            sx += c
        if sx == s:
            return x
    return minan(s, n + 1)


v = 0
for i in range(int(input())):
    v = f(int(input()), v)
    print(v)
