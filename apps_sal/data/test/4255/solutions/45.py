edges = list(map(int, input().split()))
edges.sort()
print(edges[0] * edges[1] // 2)
