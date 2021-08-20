n = int(input())
graph = [[] for i in range(n)]
l = list(map(int, input().split(' ')))
for i in range(n - 1):
    graph[i + 1] += [l[i] - 1]
    graph[l[i] - 1] += [i + 1]
cc = list(map(int, input().split(' ')))
ll = list(range(n))
colors = [0 for i in range(n)]
counter = 0
visited = [False for i in range(n)]
ans = 0
counter = 0
q = [i]
visited[i] = True
while len(q) != 0:
    u = q[0]
    q.pop(0)
    for j in graph[u]:
        if visited[j]:
            continue
        if cc[j] != cc[u]:
            counter += 1
        visited[j] = True
        q += [j]
print(counter + 1)
