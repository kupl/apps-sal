import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 1


def resolve():
    def dfs(v, p, c):
        nonlocal res
        res = (res * c) % mod
        c = k - 1 if p == -1 else k - 2
        for u in edge[v]:
            if u != p:
                dfs(u, v, c)
                c -= 1

    n, k = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    dfs(0, -1, k)
    print(res)


def __starting_point():
    resolve()


__starting_point()
