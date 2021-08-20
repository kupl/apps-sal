def xgcd(a, b):
    (x0, y0, x1, y1) = (1, 0, 0, 1)
    while b != 0:
        (q, a, b) = (a // b, b, a % b)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return x0


def modinv(a, m):
    x = xgcd(a, m)
    return x % m


max_num = 10 ** 9 + 7
res = 0
(n, m, k) = list(map(int, input().strip().split()))
for d in range(1, n):
    res += (n - d) * d * m * m
    res %= max_num
for d in range(1, m):
    res += (m - d) * d * n * n
    res %= max_num
r = min(n * m - 2, k - 2)
for i in range(1, r + 1):
    res *= n * m - 1 - i
    res %= max_num
for i in range(1, r + 1):
    res *= modinv(i, max_num)
    res %= max_num
print(res)
