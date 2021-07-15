r1, c1, r2, c2 = map(int, input().split())
MOD = 10**9 + 7

def factorial(n, mod=10**9+7):
    a = 1
    for i in range(1,n+1):
        a = a * i % mod
    return a


def power(n, r, mod=10**9+7):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


def comb(n, k, mod=10**9+7):
    if n < k or k < 0:
        result = 0
    else:
        a = factorial(n, mod=mod)
        b = factorial(k, mod=mod)
        c = factorial(n-k, mod=mod)
        result = (a * power(b, mod-2, mod=mod) * power(c, mod-2, mod=mod)) % mod
    return result


def g(r, c):
  return comb(c+r+2, r+1) - 1

ans = g(r2, c2) - g(r2, c1-1) - g(r1-1, c2) + g(r1-1, c1-1)
ans %= MOD
print(ans)
