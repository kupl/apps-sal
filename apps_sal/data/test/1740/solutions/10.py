n = int(input())
parent = [i for i in range(n + 1)]
group = [[i] for i in range(n + 1)]
for i in range(n - 1):
    (x, y) = list(map(int, input().split()))
    if len(group[parent[x]]) < len(group[parent[y]]):
        (x, y) = (y, x)
    group[parent[x]] += group[parent[y]]
    for j in group[parent[y]]:
        parent[j] = parent[x]
print(*group[parent[1]])
