n = int(input())
graph = list()
for i in range(n):
    graph.append(set())
for j in range(n - 1):
    v1, v2 = list(map(int, input().split()))
    graph[v1 - 1].add(v2)
    graph[v2 - 1].add(v1)
result = 0
for k in range(n):
    d = len(graph[k])
    result += d * (d - 1) / 2
print(int(result))
