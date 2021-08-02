# AOJ GRL_6_A "Maximum Flow"
# Ford-Fulkerson method

import sys
input = sys.stdin.readline

INF = 10**18

H, W = map(int, input().split())
V = H + W


def make():
    state = [list(input().rstrip()) for _ in range(H)]
    graph = [{} for _ in range(V + 2)]

    start = V
    finish = V + 1

    for h in range(H):
        for w in range(W):
            u, v = h, w + H
            if state[h][w] == "o":
                graph[u][v] = 1
                graph[v][u] = 1
            if state[h][w] == "S":
                graph[v][start] = INF
                graph[start][v] = INF
                graph[u][start] = INF
                graph[start][u] = INF
            if state[h][w] == "T":
                graph[u][finish] = INF
                graph[finish][u] = INF
                graph[v][finish] = INF
                graph[finish][v] = INF

    return graph, start, finish


def dfs2(start, finish, graph):
    Flow = [INF] * len(graph)
    used = [False] * len(graph)
    Par = [-1] * len(graph)
    stack = [start]
    used[start] = True
    while stack:
        v = stack.pop()
        if v == finish:
            d = Flow[v]
            while v != start:
                nv = Par[v]
                graph[nv][v] -= d
                graph[v][nv] += d
                v = nv
            return d, graph
        for i, (nv, ncap) in enumerate(graph[v].items()):
            if not used[nv] and ncap > 0:
                used[nv] = True
                stack.append(nv)
                Par[nv] = v
                Flow[nv] = min(Flow[v], ncap)
    return 0, graph

# solve


def max_flow(start, finish, graph):
    flow = 0
    while True:
        f, graph = dfs2(start, finish, graph)
        if f == 0: return flow
        flow += f


def main():
    graph, start, finish = make()
    ans = max_flow(start, finish, graph)

    if ans > INF // 2:
        print(-1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
