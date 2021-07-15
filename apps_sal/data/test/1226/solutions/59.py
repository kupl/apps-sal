import functools
N, A, B = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def modpow(x, n):
    ret = 1
    while n:
        if n & 1:
            ret = ret * x % MOD
        x = x * x % MOD
        n >>= 1
    return ret

@functools.lru_cache(maxsize=None)
def modinv(x):
    return modpow(x, MOD - 2)

def modcomb(n, r):
    ret = 1
    for i in range(n, n - r, -1):
        ret *= i
        ret %= MOD
    for i in range(r, 1, -1):
        ret *= modinv(i)
        ret %= MOD
    return ret

total = modpow(2, N) - 1
ans = total - (modcomb(N, A) + modcomb(N, B))
ans %= MOD
print(ans)

