
from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for i in range(n - 1):
    l = list(map(int, input().split()))
    graph[l[0]].append(l[1])
    graph[l[1]].append(l[0])
color_v = [-1] * (n + 1)
color_v[1] = 0
q = [1]
while q:
    x = q.pop()
    for i in graph[x]:
        if color_v[i] == -1:
            color_v[i] = 1 - color_v[x]
            q.append(i)
print(min(color_v.count(1), color_v.count(0)) - 1)
