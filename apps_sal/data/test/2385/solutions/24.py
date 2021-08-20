def COMinit(n, MOD):
    fact = [1, 1]
    fact_inv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % MOD)
        inv.append(-inv[MOD % i] * (MOD // i) % MOD)
        fact_inv.append(fact_inv[-1] * inv[i] % MOD)
    return (fact, fact_inv)


MOD = 10 ** 9 + 7


def resolve():

    def dfs1(r_topo, par):
        for idx in reversed(r_topo):
            for to in G[idx]:
                if to == par[idx]:
                    continue
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        (a, b) = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)
    (fact, fact_inv) = COMinit(N, MOD)
    topo = []
    P = [-1] * N
    node = [0]
    while node:
        v = node.pop()
        topo.append(v)
        for to in G[v]:
            if to == P[v]:
                continue
            P[to] = v
            node.append(to)
    size = [1] * N
    for e in reversed(topo):
        if e == 0:
            break
        size[P[e]] += size[e]
    dp1 = [1] * N
    for e in reversed(topo):
        dp1[e] = dp1[e] * fact[size[e] - 1] % MOD
        if e == 0:
            break
        dp1[P[e]] = dp1[P[e]] * dp1[e] % MOD * fact_inv[size[e]] % MOD
    dp2 = [0] * N
    dp2[0] = dp1[0]
    for e in topo[1:]:
        p = P[e]
        tmp = dp2[p] * fact[N - 1 - size[e]] % MOD * fact[size[e]] % MOD
        red = tmp * fact_inv[N - 1] % MOD * pow(dp1[e], MOD - 2, MOD) % MOD
        size_red = N - size[e]
        tmp = dp1[e] * red % MOD * fact[N - 1] % MOD
        dp2[e] = tmp * fact_inv[size[e] - 1] % MOD * fact_inv[size_red] % MOD
    print(*dp2, sep='\n')


def __starting_point():
    resolve()


__starting_point()
