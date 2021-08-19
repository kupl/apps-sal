import sys

sys.setrecursionlimit(10**7)


def dfs(s, to, color):
    for next_v, step in to[s]:
        if color[next_v] == -1:
            if step % 2 == 0:
                color[next_v] = color[s]
            else:
                color[next_v] = color[s] ^ 1
            dfs(next_v, to, color)


def solve():
    N = int(input())
    to = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        to[u].append([v, w])
        to[v].append([u, w])

    color = [-1] * N  # -1: 未探索、0: 白、1: 黒
    color[0] = 0
    dfs(0, to, color)
    print(*color, sep='\n')


def __starting_point():
    solve()


__starting_point()
