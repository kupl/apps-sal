import sys
sys.setrecursionlimit(10**9)


N = int(input())
to = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    to[u].append([v, w])
    to[v].append([u, w])


def dfs(v, color):
    for nv, w in to[v]:
        if color[nv] == -1:
            color[nv] = color[v] ^ (w % 2)
            dfs(nv, color)


def main():
    color = [-1] * N
    color[0] = 0
    dfs(0, color)
    print(*color, sep='\n')


def __starting_point():
    main()
__starting_point()
