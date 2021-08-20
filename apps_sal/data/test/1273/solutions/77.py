import sys
sys.setrecursionlimit(10010010)


def abc146_d():
    n = int(input())
    Q = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
    deg = [0] * n
    adj = [[] for _ in range(n)]
    color = dict()
    for (a, b) in Q:
        deg[a] += 1
        deg[b] += 1
        adj[a].append(b)
        adj[b].append(a)

    def dfs(s, p):
        nouse = -1
        if p > -1:
            nouse = color[min(s, p), max(s, p)]
        c = 1
        for t in adj[s]:
            if t == p:
                continue
            if c == nouse:
                c += 1
            color[min(s, t), max(s, t)] = c
            dfs(t, s)
            c += 1
    dfs(1, -1)
    print(max(deg))
    for (a, b) in Q:
        print(color[a, b])


def __starting_point():
    abc146_d()


__starting_point()
