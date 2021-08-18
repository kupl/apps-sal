from collections import defaultdict

n = int(input())
edges = defaultdict(int)
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    edges[a] += 1
    edges[b] += 1

for key in edges:
    if edges[key] == 2:
        print('NO')
        return

print('YES')
