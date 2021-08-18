import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def main():
    n = int(input())

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod
    mod = 10**9 + 7
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, n + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    ki = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        ki[a].append(b)
        ki[b].append(a)
    memo = {}

    def dfs(p, v):
        if (p, v) in memo:
            return memo[(p, v)]
        size, pat = 0, 1
        tmps, tmpp = 1, 1
        deg = len(ki[v])
        for nv in ki[v]:
            if nv == p:
                continue
            si, pi = dfs(v, nv)
            size += si
            tmps *= g2[si]
            tmps %= mod
            tmpp *= pi
            tmpp %= mod
        pat = (g1[size] * tmps * tmpp) % mod
        memo[(p, v)] = (size + 1, pat)
        return (size + 1, pat)
    ans = [0] * n

    def bfs(p, v, res):
        if p != -1:
            memo[(v, p)] = res
        deg = len(ki[v])
        tmps, tmpp = 1, 1
        for i in range(deg):
            si, pi = memo[(v, ki[v][i])]
            tmps *= g2[si]
            tmpp *= pi
            tmps %= mod
            tmpp %= mod

        ans[v] = g1[n - 1] * tmps * tmpp
        ans[v] %= mod

        dpl = [1] * (deg + 1)
        dpr = [1] * (deg + 1)
        tmp = 1
        for i in range(deg):
            si, pi = memo[(v, ki[v][i])]
            tmp *= pi * g2[si]
            tmp %= mod
            dpl[i + 1] = tmp
        tmp = 1
        for i in range(deg - 1, -1, -1):
            si, pi = memo[(v, ki[v][i])]
            tmp *= pi * g2[si]
            tmp %= mod
            dpr[i] = tmp
        for i in range(deg):
            nv = ki[v][i]
            if p == nv:
                continue
            bfs(v, nv, (n - memo[(v, nv)][0], (g1[n - 1 - memo[(v, nv)][0]] * dpl[i] * dpr[i + 1]) % mod))
    dfs(-1, 0)
    bfs(-1, 0, 0)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
