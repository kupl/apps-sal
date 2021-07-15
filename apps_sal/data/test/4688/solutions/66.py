MOD = 10**11

def fast_pow(x, n, MOD):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


n, k = map(int,input().split())
if n == 1:
    print(k)
else:
    print(k * fast_pow(k-1, n-1, MOD))
