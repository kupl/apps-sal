from collections import defaultdict, deque

NONE = -1
WHITE = 0
BLACK = 1
nw = 0


def colorize(G, color, v, c):
    nonlocal nw
    nw += (c == WHITE)
    color[v] = c
    for u in G[v]:
        if color[u] == NONE:  # not assigned a color yet
            colorize(G, color, u, 1-c)


def colorize_v2(G, stack, color):
    nw = 0
    while stack:
        v, c = stack.pop()
        color[v] = c
        nw += (c == WHITE)
        for u in G[v]:
            if color[u] == NONE:
                stack.append((u, 1-c))

    return nw


n = int(input())

# Adjacency list presentation of the graph, in which G[u] is a list of u's adjacent vertices.
G = defaultdict(list)
for _ in range(n-1):
    u, v = (int(x) for x in input().strip().split())
    G[u].append(v)
    G[v].append(u)

color = [NONE] * (n+1)
stack = deque()
stack.append((1, WHITE))
nw = colorize_v2(G, stack, color)
print(min(nw, n-nw)-1)

