n, m, s, t = [int(x) for x in input().split()]
s -= 1
t -= 1
graph = []
for i in range(n):
    graph.append([])
for i in range(m):
    v, u = [int(x) - 1 for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
head = 0
q = [s]
used = [0] * n
ds = [0] * n
ds[s] = 0
used[s] = 1
while head != n:
    parent = q[head]
    head += 1
    for child in graph[parent]:
        if not used[child]:
            q.append(child)
            used[child] = 1
            ds[child] = ds[parent] + 1
head = 0
q = [t]
used = [0] * n
used[t] = 1
dt = [0] * n
dt[t] = 0
while head != n:
    parent = q[head]
    head += 1
    for child in graph[parent]:
        if not used[child]:
            q.append(child)
            used[child] = 1
            dt[child] = dt[parent] + 1
short = ds[t]
count = 0
for v in range(n):
    for u in range(v, n):
        if dt[u] + ds[v] + 1 >= short and ds[u] + dt[v] + 1 >= short and u != v and v not in graph[u]:
            count += 1
print(count)
