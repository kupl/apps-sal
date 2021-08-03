graph, num = {}, 0
n = int(input())
for i in range(n - 1):
    a, b = [int(i) for i in input().split()]
    if a not in graph:
        graph[a] = []
    graph[a].extend([b])
    if b not in graph:
        graph[b] = []
    graph[b].extend([a])

for key in graph:
    if len(graph[key]) == 1:
        num += 1

print(num)
