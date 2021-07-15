import sys
from collections import defaultdict

# ----------

sys.setrecursionlimit(10 ** 7)
INF = float("inf")
MOD = 10 ** 9 + 7


def combination(n, k):
    if k > n - k:
        return combination(n, n - k)
    return fact[n] * ifact[k] * ifact[n - k]


def permitation(n, k):
    # nPk = nCk * k!
    if n < 0:
        return 0
    res = combination(n, k) * fact[k]
    return res % MOD


N, K = list(map(int, input().split()))
to = defaultdict(list)
for i in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

# nまでの階乗を前処理
n = 200005
fact = defaultdict(int)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i
    fact[i] %= MOD
# nまでの階乗の逆元を前処理
ifact = defaultdict(int)
ifact[n] = pow(fact[n], MOD - 2, MOD)
for i in reversed(list(range(1, n + 1))):
    ifact[i - 1] = ifact[i] * i
    ifact[i - 1] %= MOD


def dfs(v, p=-1):
    nonlocal ans
    for u in to[v]:
        if u == p:
            continue
        dfs(u, v)
    if p == -1:
        nk = K
        c = len(to[v]) + 1
    else:
        nk = K - 2
        c = len(to[v]) - 1
    ans *= permitation(nk, c)
    ans %= MOD


ans = 1
dfs(0)
print(ans)

