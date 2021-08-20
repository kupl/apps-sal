def our_sum(a, n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        q = our_sum(a, n // 2)
        return (q + q * pow(a, n // 2, mod)) % mod
    else:
        return (our_sum(a, n - 1) + pow(a, n - 1, mod)) % mod


(a, b, n, x) = map(int, input().split())
mod = 10 ** 9 + 7
res = pow(a, n, mod) * x
res %= mod
if a != 1:
    res += our_sum(a, n) * b % mod
else:
    res += b * n % mod
res %= mod
print(res)
