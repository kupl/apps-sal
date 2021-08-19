import sys
sys.setrecursionlimit(200000)
n = int(input())
l = [list(map(int, input().split())) for _ in range(n - 1)]
(q, k) = list(map(int, input().split()))
k -= 1
tree = [[] for _ in range(n)]
for (a, b, c) in l:
    a -= 1
    b -= 1
    tree[a].append([b, c])
    tree[b].append([a, c])
bit = [0 for _ in range(n)]
depth = [0 for _ in range(n)]


def dfs(v, d=0):
    bit[v] = 1
    depth[v] = d
    for (j, k) in tree[v]:
        if bit[j] == 0:
            dfs(j, d + k)


dfs(k)
for _ in range(q):
    (x, y) = list(map(int, input().split()))
    x -= 1
    y -= 1
    print(depth[x] + depth[y])
