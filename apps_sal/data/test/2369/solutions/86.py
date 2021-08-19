from collections import defaultdict, Counter
MOD = 10 ** 9 + 7
(n, K) = list(map(int, input().split()))
cnt = Counter(list(map(int, input().split())))
keys = sorted(cnt.keys())
key_to_idx = defaultdict(int)
for (i, k) in enumerate(keys):
    key_to_idx[k] = i
Acum = [0]
for k in keys:
    Acum.append(Acum[-1] + cnt[k])
U = n
fact = [0] * (U + 1)
fact[0] = 1
for i in range(1, U + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact = [0] * (U + 1)
invfact[U] = pow(fact[U], MOD - 2, MOD)
for i in reversed(list(range(U))):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def nCr(n, r):
    if r < 0 or n < r:
        return 0
    return fact[n] * invfact[r] * invfact[n - r]


ans = 0
for k in keys:
    x = Acum[key_to_idx[k] + 1]
    y = Acum[key_to_idx[k]]
    cmax = nCr(x, K) - nCr(y, K)
    cmin = nCr(n - y, K) - nCr(n - x, K)
    ans += k * (cmax - cmin)
    ans %= MOD
print(ans)
