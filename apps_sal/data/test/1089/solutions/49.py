def sum_distance(a, b):
    x = 0
    for i in range(a):
        x += (i + 1) * (a - i)
        x %= mod
    x *= pow(b, 2)
    return x % mod


def comb(n, r):
    (x, y) = (1, 1)
    for i in range(n, n - r, -1):
        x *= i
        y *= i + r - n
        x %= mod
        y %= mod
    return pow(y, mod - 2, mod) * x % mod


(n, m, k) = map(int, input().split())
mod = pow(10, 9) + 7
ans = 0
ans += sum_distance(n - 1, m)
ans += sum_distance(m - 1, n)
ans %= mod
ans *= comb(n * m - 2, k - 2)
ans %= mod
print(ans)
