import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *AB = list(map(int, read().split()))
    G = [[] for _ in range(N)]
    for a, b in zip(AB[::2], AB[1::2]):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    COM_MAX = K

    fac, finv, inv = [0] * (COM_MAX + 1), [0] * (COM_MAX + 1), [0] * (COM_MAX + 1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2, COM_MAX + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    def mod_perm(n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return fac[n] * (finv[n - r] % MOD) % MOD

    stack = deque([0])
    order = []
    parent = [-1] * N
    while stack:
        v = stack.pop()
        order.append(v)
        for nv in G[v]:
            if nv != parent[v]:
                stack.append(nv)
                parent[nv] = v

    A = [0] * N
    for v in reversed(order):
        tmp = 1
        child = 0
        for nv in G[v]:
            if nv != parent[v]:
                tmp = tmp * A[nv] % MOD
                child += 1

        colors = K if v == 0 else K - 2
        nodes = child + 1 if v == 0 else child

        A[v] = tmp * mod_perm(colors, nodes) % MOD

    print((A[0]))
    return


def __starting_point():
    main()

__starting_point()
