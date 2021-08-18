import sys

stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


sys.setrecursionlimit(100005)

n, k = na()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = na()
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

mod = 10**9 + 7


def dfs(cur, par, k, g):
    ret = 1
    nc = 0 if par == -1 else 1
    for e in g[cur]:
        if e == par:
            continue
        nc += 1
        ret = ret * (k - nc) % mod
        ret = ret * dfs(e, cur, k, g) % mod
    return ret % mod


print((dfs(0, -1, k, g) * k % mod))
