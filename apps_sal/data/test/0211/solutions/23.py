b = 10**9 + 9


def f(q):
    x = q // 1000
    y = q % 1000
    num = 2**1000 % b
    res = 1
    for i in range(x):
        res = (res * num) % b
    res = (res * 2**y) % b
    return res


def F(n, m, k):
    r = n % k
    if m <= n // k * (k - 1) + r:
        print(m % b)
    else:
        q = m - (n // k * (k - 1) + r)
        print((m + (f(q + 1) - q - 2) * k) % b)


n, m, k = [int(x) for x in input().split(' ')]
F(n, m, k)
