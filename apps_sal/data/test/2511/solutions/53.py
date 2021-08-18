import sys


sys.setrecursionlimit(10 ** 6)


def main():
    MOD = 10 ** 9 + 7
    N, K = list(map(int, input().split(' ')))
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list(map(lambda x: int(x) - 1, input().split(' ')))
        adj[a].append(b)
        adj[b].append(a)
    if K <= 2:
        if N <= K:
            p = 1
            for n in range(N):
                p *= K - n
            print(p % MOD)
        else:
            print(0)
        return
    p = 1
    perm_k1 = [0 for _ in range(K)]
    for k in range(K):
        perm_k1[k] = p
        p *= K - 1 - k
        p %= MOD
    perm_k2 = [0 for _ in range(K - 1)]
    p = 1
    for k in range(K - 1):
        perm_k2[k] = p
        p *= K - 2 - k
        p %= MOD

    def dfs(n=0, p=-1):
        children = [c for c in adj[n] if c != p]
        if len(children) == 0:
            return 1
        n_colors = K - 2 if n != 0 else K - 1
        if n_colors < len(children):
            return 0
        ret = perm_k2[len(children)] if n != 0 else perm_k1[len(children)]
        for c in children:
            ret *= dfs(c, n)
            ret %= MOD
        return ret

    print((K * dfs()) % MOD)


def __starting_point():
    main()


__starting_point()
