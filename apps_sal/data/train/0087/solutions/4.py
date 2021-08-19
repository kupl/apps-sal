from math import gcd


def sum_of_floor(n, p, q):
    t = gcd(p, q)
    (p, q) = (p // t, q // t)
    s = 0
    z = 1
    while q > 0 and n > 0:
        t = p // q
        s = s + z * t * n * (n + 1) // 2
        p = p - q * t
        t = n // q
        s = s + z * p * t * (n + 1) - z * t * (p * q * t + p + q - 1) // 2
        n = n - q * t
        t = n * p // q
        s = s + z * t * n
        n = t
        (p, q) = (q, p)
        z = -z
    return s


def solve():
    (m, d, w) = map(int, input().split())
    if d == 1:
        print(0)
        return
    u = gcd(d - 1, w)
    res = sum_of_floor(min(m, d) - 1, 1, w // u)
    print(res)


t = int(input())
for _ in range(t):
    solve()
