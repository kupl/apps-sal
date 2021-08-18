def rerooting(n, edges, identity, merge, add_node):
    G = [[] for _ in range(n)]
    G_idxs = [[] for _ in range(n)]
    for a, b in edges:
        G_idxs[a].append(len(G[b]))
        G_idxs[b].append(len(G[a]))
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
    subtree_res = [[0] * len(Gv) for Gv in G]
    for v in order[:0:-1]:
        p = parents[v]
        result = identity
        for idx_Gv, (u, subtree_res_v_i) in enumerate(zip(G[v], subtree_res[v])):
            if p == u:
                parent_idx = idx_Gv
            else:
                result = merge(result, subtree_res_v_i)
        idx_p2v = G_idxs[v][parent_idx]
        subtree_res[p][idx_p2v] = add_node(result, v)
    results = [0] * n
    for v in order:
        subtree_res_v = subtree_res[v]
        cum = identity
        cum_from_tail = [identity]
        for r in subtree_res_v[:0:-1]:
            cum = merge(r, cum)
            cum_from_tail.append(cum)
        cum_from_tail.reverse()
        cum = identity
        for r, cum_t, u, idx_u2v in zip(subtree_res_v, cum_from_tail, G[v], G_idxs[v]):
            result = add_node(merge(cum, cum_t), v)
            subtree_res[u][idx_u2v] = result
            cum = merge(cum, r)
        results[v] = add_node(cum, v)
    return results


class Combination:
    def __init__(self, n_max, mod=10**9 + 7):
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
    mod = 10**9 + 7
    comb = Combination(202020)
    identity = (1, 0)
    def merge(a, b): return (a[0] * b[0] % mod * comb(a[1] + b[1], a[1]) % mod, a[1] + b[1])
    def add_node(value, idx): return (value[0], value[1] + 1)
    Ans = rerooting(N, AB, identity, merge, add_node)
    print(("\n".join(str(ans) for ans, _ in Ans)))


main()
