import sys
sys.setrecursionlimit(500 * 500)

N = int(input())


edges = [list(map(int, input().split())) for _ in range(N - 1)]
tree = [[] for _ in range(N + 1)]

for edge in edges:
    tree[edge[0]].append([edge[1], edge[2]])
    tree[edge[1]].append([edge[0], edge[2]])


depth = [-1] * (N + 1)
depth[1] = 0


def dfs(tree, s):
    for l in tree[s]:
        if depth[l[0]] == -1:
            depth[l[0]] = depth[s] + l[1]
            dfs(tree, l[0])


dfs(tree, 1)


for l in depth[1:]:
    if l % 2 == 0:
        print((1))
    else:
        print((0))
