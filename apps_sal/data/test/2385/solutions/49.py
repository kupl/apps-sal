from functools import reduce


def rerooting(n, edges, identity, merge, add_node):
    from functools import reduce
    G = [[] for _ in range(n)]
    for (a, b) in edges:
        G[a].append(b)
        G[b].append(a)
    parents = [0] * n
    order = []
    stack = [0]
    parents[0] = -1
    while stack:
        v = stack.pop()
        p = parents[v]
        order.append(v)
        for u in G[v]:
            if p != u:
                stack.append(u)
                parents[u] = v
    dp_down = [0] * n
    for v in order[:0:-1]:
        p = parents[v]
        dp_down[v] = add_node(reduce(merge, (dp_down[u] for u in G[v] if u != p), identity), v)
    dp_up = [identity] * n
    for v in order:
        Gv = G[v]
        if len(Gv) == 1 and v != 0:
            continue
        p = parents[v]
        cum = identity
        right = [identity]
        for u in Gv[::-1]:
            if u != p:
                cum = merge(dp_down[u], cum)
                right.append(cum)
        cum = dp_up[v]
        idx_right = -2
        for u in Gv:
            if u != p:
                dp_up[u] = add_node(merge(cum, right[idx_right]), v)
                idx_right -= 1
                cum = merge(cum, dp_down[u])
    results = [add_node(merge(reduce(merge, (dp_down[u] for u in Gv if u != parents[v]), identity), dp_up[v]), v) for (v, Gv) in enumerate(G)]
    return results


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

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod


def main():
    N = int(input())
    AB = [list([int(x) - 1 for x in input().split()]) for _ in range(N - 1)]
    mod = 10 ** 9 + 7
    comb = Combination(202020)
    identity = (1, 0)
    (fac, facinv) = (comb.fac, comb.facinv)

    def merge(a, b):
        (a0, a1) = a
        (b0, b1) = b
        return (a0 * b0 * fac[a1 + b1] * facinv[a1] * facinv[b1] % mod, a1 + b1)

    def add_node(a, idx):
        (a0, a1) = a
        return (a0, a1 + 1)
    Ans = rerooting(N, AB, identity, merge, add_node)
    print('\n'.join((str(ans) for (ans, _) in Ans)))


main()
