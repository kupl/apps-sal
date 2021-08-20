n = int(input())
edges = [int(x) - 1 for x in input().split()]
visited = [False for _ in range(n)]
sizes = []
for i in range(n):
    if visited[i]:
        continue
    visited[i] = True
    component_size = 1
    j = edges[i]
    while not visited[j]:
        visited[j] = True
        component_size += 1
        j = edges[j]
    sizes.append(component_size)
sizes = sorted(sizes)
if len(sizes) > 1:
    sizes[-2] += sizes[-1]
    sizes.pop()
print(sum([x ** 2 for x in sizes]))
