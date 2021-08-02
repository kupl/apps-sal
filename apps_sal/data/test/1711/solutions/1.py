n, m = map(int, input().split())

if n < 3:
    print(0)
    return

mod = 998244353


def C(n, k):
    if k > n: return 0
    k = min(k, n - k)
    a = 1
    b = 1
    for i in range(k):
        a = (a * (n - i)) % mod
        b = (b * (i + 1)) % mod
    return (a * pow(b, mod - 2, mod)) % mod


a = ((n - 2) * pow(2, n - 3, mod)) % mod
b = (m - n + 2) * C(m, n - 2)
b = (b * pow(n - 1, mod - 2, mod)) % mod

ans = (a * b) % mod
print(ans)
