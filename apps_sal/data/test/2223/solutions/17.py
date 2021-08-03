n = int(input())
if n % 2 == 1:
    print(-1)
    return
graph = {}
for i in range(n - 1):
    v, u = map(int, input().strip().split())
    v -= 1
    u -= 1
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
countArr = [1 for i in range(n)]
s = [0]
vis = [-1 for i in range(n)]
while s:
    curr = s[-1]
    k = False
    for i in graph[curr]:
        if vis[i] == -1:
            vis[i] = curr
            s.append(i)
            k = True
    if not k:
        if curr != 0:
            countArr[vis[curr]] += countArr[curr]
        s.pop()
o = 0
for i in countArr[1:]:
    if i % 2 == 0:
        o += 1
print(o)
