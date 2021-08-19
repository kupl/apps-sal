import sys
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = 1 << 50
EPS = 1e-08
mod = 10 ** 9 + 7


def intread():
    return int(sysread())


def mapline(t=int):
    return list(map(t, sysread().split()))


def mapread(t=int):
    return list(map(t, read().split()))


def dfs(current, to, dists):
    (c, c_cost) = current
    dists[c] = c_cost
    for (n, n_cost) in to[c]:
        if dists[n] == -1:
            dfs((n, c_cost + n_cost), to, dists)
    return dists


def run():
    N = intread()
    to = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        (a, b, c) = mapline()
        to[a].append((b, c))
        to[b].append((a, c))
    (Q, K) = mapline()
    dists = [-1] * (N + 1)
    dists = dfs((K, 0), to, dists)
    for i in range(Q):
        (x, y) = mapline()
        print(dists[x] + dists[y])


def __starting_point():
    run()


__starting_point()
