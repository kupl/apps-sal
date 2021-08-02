MOD = 998244353
n = int(input())
if n < 3:
    print(n)
else:
    mxm = 9
    m = 3
    mf = 6
    for _ in range(n - 3):
        m += 1
        mxm = (mxm + 1) * m
        mxm %= MOD
        mf *= m
        mf %= MOD
    print((n * mf - mxm) % MOD)
