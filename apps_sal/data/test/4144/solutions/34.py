n = int(input())

mod = 10**9 + 7


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        n = n >> 1
    return res


ans = (modpow(10, n, mod) - modpow(9, n, mod) -
       modpow(9, n, mod) + modpow(8, n, mod)) % mod
print(ans)
