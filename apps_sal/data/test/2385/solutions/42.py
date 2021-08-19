
"""
Writer: SPD_9X2
https://atcoder.jp/contests/abc160/tasks/abc160_f

全方位木dpの実装はどうしよう？
まず0について求め、必要な値を取っておいて、親に近い方から親の値を使って求める
がよさそう


かけるべきは、 N-1 C (N-小部分木に含まれる頂点数) * 親の答え // (小部分木のmu* N-1C小部分木の頂点数)
"""
import sys
sys.setrecursionlimit(10 ** 6)


def inverse(a, mod):  # aのmodを法にした逆元を返す
    return pow(a, mod - 2, mod)


# modのn!と、n!の逆元を格納したリストを返す(拾いもの)
# factorialsには[1, 1!%mod , 2!%mod , 6!%mod… , n!%mod] が入っている
# invsには↑の逆元が入っている

def modfac(n, MOD):

    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs


def modnCr(n, r, mod, fac, inv):  # 上で求めたfacとinvsを引数に入れるべし(上の関数で与えたnが計算できる最大のnになる)

    return fac[n] * inv[n - r] * inv[r] % mod


N = int(input())
mod = 10**9 + 7
fac, inv = modfac(N, mod)

lis = [[] for i in range(N)]

for i in range(N - 1):

    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1

    lis[a].append(b)
    lis[b].append(a)

plis = [i for i in range(N)]
chnum = [0] * N
mulis = [0] * N


def dfs(v, p):

    rch = 1
    rmu = 1
    chlis = []

    for nex in lis[v]:

        if nex != p:

            ch, mu = dfs(nex, v)
            rch += ch
            rmu *= mu
            rmu %= mod
            chlis.append(ch)

    nsum = sum(chlis)

    for i in range(len(chlis)):

        rmu *= modnCr(nsum, chlis[i], mod, fac, inv)
        rmu %= mod
        nsum -= chlis[i]

    plis[v] = p
    chnum[v] = rch
    mulis[v] = rmu

    return rch, rmu


ans = [None] * N

temp, ans[0] = dfs(0, 0)

#print (plis,chnum,mulis)


def dfs2(v, p):

    #print (v,p)

    if v != 0:
        vn = chnum[v]
        mn = mulis[v]

        ans[v] = ans[p] * modnCr(N - 1, N - vn, mod, fac, inv) * inverse(modnCr(N - 1, vn, mod, fac, inv), mod) % mod
    for nex in lis[v]:
        if nex != p:
            dfs2(nex, v)


dfs2(0, 0)
print(("\n".join(map(str, ans))))
