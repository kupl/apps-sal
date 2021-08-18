import sys
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
N, K = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


ans = K


def rec(c, p):
    nonlocal ans
    if c == 0:
        for i in range(len(g[0])):
            ans *= K - i - 1
            ans %= mod
        for v in g[c]:
            if v != p:
                rec(v, c)
    else:
        for i in range(len(g[c]) - 1):
            ans *= K - i - 2
            ans %= mod
        for v in g[c]:
            if v != p:
                rec(v, c)


rec(0, 0)
print(ans)
