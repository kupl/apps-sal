from sys import stdin, stdout
S = [int(z) for z in stdin.readline().strip()]
n = len(S)
graph = {}
d = {}
visited = {}
for i in range(n):
    graph[S[i]] = []
    visited[i] = 0
    d[i] = 0
if n > 1:
    for i in range(n):
        graph[S[i]].append(i)
    queue = [0]
    while len(queue) != 0:
        u = queue.pop(0)
        for v in graph[S[u]]:
            if visited[v] == 0 and v != u:
                d[v] += d[u] + 1
                queue.append(v)
                visited[v] = 1
        graph[S[u]] = []
        if u - 1 >= 0:
            if visited[u - 1] == 0:
                d[u - 1] = d[u] + 1
                visited[u - 1] = 1
                queue.append(u - 1)
        if u + 1 < n:
            if visited[u + 1] == 0:
                d[u + 1] = d[u] + 1
                visited[u + 1] = 1
                queue.append(u + 1)
        visited[u] = 1
    stdout.write('%d\n' % d[n - 1])
else:
    stdout.write('0\n')
