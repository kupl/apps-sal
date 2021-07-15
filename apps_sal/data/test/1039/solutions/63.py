import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append([b, c])
    edges[b].append([a, c])
    
q, k = map(int, input().split())

check = [False for _ in range(n)]
dist = [0 for _ in range(n)]
def dfs(pos, b_pos):
    for n_pos, c in edges[pos]:
        if n_pos == b_pos:
            continue
        check[n_pos] = True
        dist[n_pos] = c + dist[pos]
        dfs(n_pos, pos)

check[k - 1] = True
dfs(k - 1, -1)

for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(dist[x] + dist[y])
