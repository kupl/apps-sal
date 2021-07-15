import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
edge = [[] for _ in range(N)]
for i in range(N-1):
    a, b = [int(_) - 1 for _ in input().split()]
    edge[a].append((b, i))
    edge[b].append((a, i))
ans = [0] * (N - 1)
colors_num = max([len(_) for _ in edge])
colors = list(range(colors_num))


def dfs(v, pv, pc):
    valid_colors = [c for c in colors if c != pc]
    childs = list([c for c in edge[v] if c[0] != pv])
    for ((cv, ci), color) in zip(childs, valid_colors):
        ans[ci] = color + 1
        dfs(cv, v, color)


dfs(0, -1, -1)
print(colors_num)
print((*ans))

