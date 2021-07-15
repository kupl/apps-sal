MOD = 998244353
def w(a, b):
    # SUM (k = 0..min) C(a, k) * C(b, k) * k!
    rt, ca, cb, fl = 1, 1, 1, 1
    for k in range(1, min(a, b) + 1):
        fl = fl * k % MOD
        ca = ca * (a - k + 1) // k
        cb = cb * (b - k + 1) // k
        rt = (rt + ((ca % MOD) * (cb % MOD) % MOD) * fl % MOD) % MOD
    return rt

a, b, c = map(int, input().split())
print(((w(a, b) % MOD) * w(b, c) % MOD) * w(c, a) % MOD)
