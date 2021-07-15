MOD = 1000000009
def AlternateSum(n,a,b,k,s):
    res = 0
    inv = lambda x: pow(x, MOD-2, MOD)
    q = pow(b, k, MOD) * inv(pow(a, k, MOD)) % MOD
    max_pow = pow(a, n, MOD)
    c = b * inv(a) % MOD
    for i in range(k):
        if s[i] == '+':
            res += max_pow
        else:
            res -= max_pow
        res %= MOD
        max_pow = max_pow * c % MOD
    t = (n + 1) // k
    if q == 1:
        return t * res % MOD
    z = (pow(q, t, MOD) - 1) * inv(q-1) % MOD
    return z * res % MOD
n, a, b, k = [int(x) for x in input().split()]
s = input()
print(AlternateSum(n, a, b, k, s))
