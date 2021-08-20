from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def ext_euc(a, b):
    if b == 0:
        return (1, 0, a)
    (y, x, v) = ext_euc(b, a % b)
    y -= a // b * x
    return (x, y, v)


def mod_inv(a, mod):
    (x, _, _) = ext_euc(a, mod)
    return x % mod


def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    adj = defaultdict(list)
    for _ in range(N - 1):
        (A, B) = list(map(lambda x: int(x) - 1, input().split()))
        adj[A].append(B)
        adj[B].append(A)
    pow_2 = [1 for _ in range(N + 1)]
    for i in range(1, N + 1):
        pow_2[i] = pow_2[i - 1] * 2 % MOD
    node_num = defaultdict(int)

    def dfs(node=0, parent=None):
        child_list = [n for n in adj[node] if n != parent]
        if len(child_list) == 0:
            node_num[node, parent] = N - 1
            node_num[parent, node] = 1
            return 1
        n_descendant = 1
        for child in child_list:
            n_descendant += dfs(child, node)
        if parent is not None:
            node_num[node, parent] = N - n_descendant
            node_num[parent, node] = n_descendant
        return n_descendant
    dfs()
    numer = 0
    for node in range(N):
        if len(adj[node]) <= 1:
            continue
        cnt_not = 0
        for dir_node in adj[node]:
            cnt_not += pow_2[node_num[node, dir_node]]
        cnt_not -= len(adj[node]) - 1
        numer += pow_2[N - 1] - cnt_not
    denom = pow_2[N]
    print(numer * mod_inv(denom, MOD) % MOD)


def __starting_point():
    main()


__starting_point()
