"""
繰り返し2乗法
フェルマーの小定理
"""

n, a, b = list(map(int, input().split()))
MOD = (10**9) + 7


def cal(n, a):
    r = n
    sub = 1
    while a > 1:
        if a % 2 == 1:
            a -= 1
            sub = (sub * r) % MOD
        r = (r * r) % MOD
        a /= 2
    return r * sub % MOD


def felmer(n, a, b):
    r = [0, 0]
    ni = n
    ab = 1
    for i in range(1, max(a, b) + 1):
        ab = ab * i % MOD
        if i == a:
            r[0] = (ni * cal(ab, MOD - 2)) % MOD
        elif i == b:
            r[1] = (ni * cal(ab, MOD - 2)) % MOD
        ni = ni * (n - i) % MOD
    return r


allNumber = cal(2, n)
nCa, nCb = felmer(n, a, b)
ans = allNumber - 1 - nCa - nCb
ans %= MOD
if ans < 0:
    ans += MOD
print(ans)
