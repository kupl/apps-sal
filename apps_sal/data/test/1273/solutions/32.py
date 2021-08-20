import sys
import math
from collections import deque
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def make_grid(h, w, num):
    return [[int(num)] * w for _ in range(h)]


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N = NI()
    edges = [NLI() for _ in range(N - 1)]
    graph = [[] for _ in range(N + 1)]
    edge_dict = {}
    for (i, edge) in enumerate(edges):
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        edge_dict[edge[0], edge[1]] = i + 1
    queue = deque()
    queue.append(1)
    seen = [0] * (N + 1)
    colors = [-1] * N
    colors[1] = 1
    now_colors = deque()
    now_colors.append(-1)
    while queue:
        now = queue.popleft()
        now_color = now_colors.popleft()
        seen[now] = 1
        nexts = graph[now]
        color = 1
        for goto in nexts:
            if seen[goto] == 0:
                (a, b) = (min(now, goto), max(now, goto))
                if color == now_color:
                    color += 1
                colors[edge_dict[a, b]] = color
                queue.append(goto)
                now_colors.append(color)
                color += 1
    print(max(colors))
    for i in range(1, N):
        print(colors[i])


def __starting_point():
    main()


__starting_point()
