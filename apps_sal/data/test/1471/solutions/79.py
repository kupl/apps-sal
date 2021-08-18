from collections import deque
import sys

sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
sys.setrecursionlimit(10 ** 7)

INF = 1 << 50
EPS = 1e-8
mod = 998244353


def intread():
    return int(sysread())


def mapline(t=int):
    return list(map(t, sysread().split()))


def mapread(t=int):
    return list(map(t, read().split()))


def dfs(c, num, to, cols):
    for n, nw in to[c]:
        if cols[n] == -1:
            y = (num + nw) % 2
            cols[n] = (num + nw) % 2
            dfs(n, y, to, cols)


def run():
    N = intread()
    to = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = mapline()
        to[u].append((v, w))
        to[v].append((u, w))
    cols = [-1] * (N + 1)
    cols[1] = 0
    dfs(1, 0, to, cols)

    for x in cols[1:]:
        print(x)


def __starting_point():
    run()


__starting_point()
