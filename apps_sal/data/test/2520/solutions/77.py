import sys
sys.setrecursionlimit(10**9)
n, m, k = map(int, input().split())
friend = [[] for _ in range(n)]
block = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friend[a].append(b)
    friend[b].append(a)
for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    block[c].append(d)
    block[d].append(c)
seen = [-1] * n


def dfs(graph, v, top):
    seen[v] = top
    top_count[top] += 1
    for nv in graph[v]:
        if seen[nv] != -1:
            continue
        dfs(graph, nv, top)


top = 0
top_count = [0]
for v in range(n):
    count = 0
    if seen[v] != -1:
        continue
    dfs(friend, v, top)
    top_count.append(0)
    top += 1


for i in range(n):
    ans = top_count[seen[i]] - len(friend[i]) - 1
    cnt = 0
    for v in block[i]:
        if seen[v] == seen[i]:
            cnt += 1
    ans -= cnt
    print(ans, end=' ')
