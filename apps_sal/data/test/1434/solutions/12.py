__author__ = 'artyom'


def read():
    return map(int, input().split())


n = int(input())
graph = [set() for _ in range(n)]
degrees = []
adj = []
queue = []
for i in range(n):
    (degree, s) = read()
    degrees.append(degree)
    adj.append(s)
    if degree == 1:
        queue.append(i)
counter = 0
ans = ''
while queue:
    v = queue.pop()
    if degrees[v] == 0:
        continue
    s = adj[v]
    for u in graph[v]:
        s ^= u
    graph[s].add(v)
    graph[v].add(s)
    counter += 1
    ans += '\n' + str(s) + ' ' + str(v)
    degrees[s] -= 1
    if degrees[s] == 1:
        queue.append(s)
print(str(counter) + ans)
