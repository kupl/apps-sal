import sys
sys.setrecursionlimit(10**5)

n, k = map(int, input().split())
m = 10**9 + 7
to = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    to[a].append(b)
    to[b].append(a)
frac = [1] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    frac[i] = frac[i - 1] * i
    frac[i] %= m


def nPk(_n, _k):
    if _n < 0 or _k < 0 or _n - _k < 0: return 0;
    a = frac[_n]
    b = frac[_n - _k]
    return (a * pow(b, m - 2, m)) % m


def dfs(_v, _u=-1):
    nonlocal ans
    for u in to[_v]:
        if u == _u: continue
        dfs(u, _v)
    p = len(to[_v])
    ans *= nPk(k, p + 1) if _v == 0 else nPk(k - 2, p - 1)
    ans %= m


ans = 1
chk = [False] * n
dfs(0)

print(ans)
