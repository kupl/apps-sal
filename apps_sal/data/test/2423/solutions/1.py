n = int(input().strip())
graph = [[] for i in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
count = 0
for g in graph:
    if len(g) < 2:
        count += 1
print(count)
