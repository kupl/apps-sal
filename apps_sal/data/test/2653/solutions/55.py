import sys
sys.setrecursionlimit(500 * 500)
(N, Q) = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
tree = [[] for _ in range(N + 1)]
for edge in edges:
    tree[edge[0]].append(edge[1])
    tree[edge[1]].append(edge[0])
depth = [-1] * (N + 1)
depth[1] = 0
count = [0] * (N + 1)
for i in range(Q):
    (p, x) = map(int, input().split())
    count[p] += x


def dfs(tree, s):
    for l in tree[s]:
        if depth[l] == -1:
            depth[l] = 0
            count[l] += count[s]
            dfs(tree, l)


dfs(tree, 1)
for i in count[1:]:
    print(i, end=' ')
