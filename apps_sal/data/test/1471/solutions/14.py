import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u:int, v:int):
    cv = color[v]
    for s, k in graph[v]:
        if s == u:
            continue
        elif color[s] != -1:
            continue
        elif k%2 == 0:
            color[s] = cv
            dfs(v, s)
        else:
            color[s] = (cv+1)%2
            dfs(v, s)

def main():
    nonlocal color, graph
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = list(map(int, input().split()))
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    color = [-1] * N

    color[0] = 0
    dfs(-1, 0)

    for c in color:
        print(c)

def __starting_point():
    main()

__starting_point()
