from collections import defaultdict

# Combination
MOD = 10**17 + 3
MAX = 2 * 10**5
fac = [1, 1] + [0] * MAX
finv = [1, 1] + [0] * MAX
inv = [0, 1] + [0] * MAX
for i in range(2, MAX + 2):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD


N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))
V.sort(reverse=True)
arr = V[:A]
se = set()
mi = 10**18
dic2 = defaultdict(int)
tot = 0
for a in arr:
    tot += a
    dic2[a] += 1
    se.add(a)
    if a < mi:
        mi = a
dic = defaultdict(int)
for v in V:
    dic[v] += 1
if len(se) == 1:
    ans = 0
    for i in range(A, B + 1):
        ans += comb(dic[mi], i)
else:
    ans = comb(dic[mi], dic2[mi])
print((tot / A))
print(ans)
