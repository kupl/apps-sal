from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N  = int(input())
Gb = [ [] for _ in range(N) ]
Gu = [ [] for _ in range(N) ]
Es = {}

for n in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())

    Es[f'{a:06}{b:06}'] = None

    Gb[a].append(b)
    Gb[b].append(a)
    Gu[a].append(b)

colors = list(range(max(map(len, Gb))))

def dfs(base_node, edge_color):
    nonlocal Es

    valid_colors = filter(lambda color: color != edge_color, colors)

    for child_node, color in zip(Gu[base_node], valid_colors):
        Es[f'{base_node:06}{child_node:06}'] = color + 1

        dfs(child_node, color)

print(len(colors))

dfs(0, None)

for color in Es.values():
    print(color)
