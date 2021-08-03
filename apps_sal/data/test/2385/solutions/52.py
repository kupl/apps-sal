import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

U = 2 * 10**5
MOD = 10**9 + 7

fact = [1] * (U + 1)
fact_inv = [1] * (U + 1)

for i in range(1, U + 1):
    fact[i] = (fact[i - 1] * i) % MOD
fact_inv[U] = pow(fact[U], MOD - 2, MOD)

for i in range(U, 0, -1):
    fact_inv[i - 1] = (fact_inv[i] * i) % MOD

n = int(input())
T = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    T[a].append(b)
    T[b].append(a)
size = [0] * n
par = [-1] * n
dp1 = [-1] * n
dp2 = [-1] * n


def dfs1(p, v):
    if dp1[v] != -1:
        return dp1[v]
    temp = 1
    s = 1
    for nv in T[v]:
        if nv == p:
            continue
        temp *= dfs1(v, nv)
        temp *= fact_inv[size[nv]]
        temp %= MOD
        par[nv] = v
        s += size[nv]
    size[v] = s
    temp *= fact[s - 1]
    temp %= MOD
    dp1[v] = temp
    return temp


dfs1(-1, 0)


def dfs2(v):
    if v == 0:
        return dp1[0]
    if dp2[v] != -1:
        return dp2[v]
    temp = dfs2(par[v])
    temp *= fact[n - size[v] - 1]
    temp *= fact[size[v]]
    temp %= MOD
    temp *= fact_inv[size[v] - 1]
    temp *= fact_inv[n - size[v]]
    temp %= MOD
    dp2[v] = temp
    return temp


for i in range(n):
    print(dfs2(i))
