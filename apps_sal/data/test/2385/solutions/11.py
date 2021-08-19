import sys
sys.setrecursionlimit(505050)


class Combination:

    def __init__(self, n_max, mod=10 ** 9 + 7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()


N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b) = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)
Siz = [0] * (N + 1)
A = [0] * (N + 1)
mod = 10 ** 9 + 7
comb = Combination(202020)


def dfs1(v, p):
    siz = 1
    an_prod = 1
    an_numer = 0
    an_denom = 1
    for u in G[v]:
        if u != p:
            (s, a) = dfs1(u, v)
            siz += s
            an_prod = an_prod * a % mod
            an_numer += s
            an_denom = an_denom * comb.facinv[s] % mod
    an_numer = comb.fac[an_numer]
    an = an_numer * an_denom % mod * an_prod % mod
    Siz[v] = siz
    A[v] = an
    return (siz, an)


(_, ans) = dfs1(1, 0)
Ans = [0] * (N + 1)
Ans[1] = ans


def dfs2(v, p, an_p):
    siz_v = Siz[v]
    if v == 1:
        ans = A[v]
    else:
        ans = A[v] * comb.fac[N - 1] % mod * comb.facinv[siz_v - 1] % mod * an_p % mod * comb.facinv[N - siz_v] % mod
        Ans[v] = ans
    for u in G[v]:
        if p != u:
            siz_u = Siz[u]
            an = ans * comb.facinv[N - 1] % mod * comb.fac[N - 1 - siz_u] % mod * comb.fac[siz_u] % mod * pow(A[u], mod - 2, mod) % mod
            dfs2(u, v, an)


dfs2(1, 0, None)
print('\n'.join(map(str, Ans[1:])))
