import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def read():
    (N, K) = list(map(int, input().strip().split()))
    G = [[] for i in range(N + 1)]
    for i in range(N - 1):
        (a, b) = list(map(int, input().strip().split()))
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    return (N, K, G)


def permute_init(n, MOD):
    factorial = [1 for i in range(n + 1)]
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i
        factorial[i] %= MOD
    return factorial


def permute(n, r, factorial, MOD):
    """nPr = n! / (n-r)!"""
    if n < 0 or r < 0 or n < r:
        return 0
    return factorial[n] * pow(factorial[n - r], MOD - 2, MOD) % MOD


def solve(N, K, G, MOD=10 ** 9 + 7):
    factorial = permute_init(K, MOD)
    visited = [False for i in range(N)]

    def dfs(a=0):
        f = 1
        if a == 0:
            f = permute(K - 1, len(G[a]), factorial, MOD)
        else:
            f = permute(K - 2, len(G[a]) - 1, factorial, MOD)
        for b in G[a]:
            if not visited[b]:
                visited[b] = True
                f *= dfs(b)
                f %= MOD
        return f
    visited[0] = True
    ans = K * dfs(0) % MOD
    return ans


def __starting_point():
    inputs = read()
    print('%s' % solve(*inputs))


__starting_point()
