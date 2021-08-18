from collections import defaultdict
graph = defaultdict(list)
n, m, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
d = {}
visited = [False for i in range(n)]
for i in arr:
    cur = i
    q = []
    d[cur] = []
    q.append(cur)
    visited[cur - 1] = True
    while q != []:
        u = q.pop(0)
        d[cur].append(u)
        for j in graph[u]:
            if visited[j - 1] == False:
                visited[j - 1] = True
                q.append(j)
visited = [False for i in range(n)]
for i in d:
    for j in d[i]:
        visited[j - 1] = True
rem = 0
for i in visited:
    if i == False:
        rem += 1
ans = []
for i in d:
    ans.append(len(d[i]))
ans.sort()
ans[-1] += rem
tmp = 0
for i in ans:
    tmp += (i * (i - 1)) // 2
print(tmp - m)
