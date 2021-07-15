
from collections import defaultdict
n, m = list(map(int, input().split()))
graph = defaultdict(set)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].add(b)
    graph[b].add(a)
 
ans = 100
for i in range(1, 7):
    for j in range(i + 1, 8):
        g = graph[i] & graph[j]
        ans = min(ans, len(g))
print(m - ans)

