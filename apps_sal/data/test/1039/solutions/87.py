import sys
sys.setrecursionlimit(10**7)

N = int(input())
tree = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, c = list(map(int, input().split()))
    tree[a - 1].append([b - 1, c])
    tree[b - 1].append([a - 1, c])
Q, K = list(map(int, input().split()))

dist = [-1] * N


def dfs(v, total_cost):
    dist[v] = total_cost
    for v_next, cost in tree[v]:
        if dist[v_next] >= 0:
            continue
        dfs(v_next, total_cost + cost)


dfs(K - 1, 0)

for i in range(Q):
    x, y = list(map(int, input().split()))
    print((dist[x - 1] + dist[y - 1]))
