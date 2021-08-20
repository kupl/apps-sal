k = int(input())


def s(n):
    r = 0
    while n > 0:
        r += n % 10
        n = n // 10
    return r


def find_next(n):
    d = 0
    m = n // 10
    sm = s(m)
    r = 0
    grad = 10 * m + 1 - sm - 9 * d - 1 / 10 ** d
    while grad > 0:
        r += 9 * 10 ** d
        d += 1
        sm -= m % 10
        m = m // 10
        grad = 10 * m + 1 - sm - 9 * d - 1 / 10 ** d
    r += n // 10 ** d * 10 ** d
    return r


for i in range(1, min(k, 9) + 1):
    print(i)
k -= min(k, 9)
p = 10
for i in range(0, k):
    p = find_next(p)
    print(p)
    p += 1
