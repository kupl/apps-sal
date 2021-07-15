from collections import defaultdict, deque
import sys

n = int(input())
a = [int(val) for val in input().split()]
a = [val for val in a if val > 0]
n = len(a)

count = defaultdict(list)
for i, val in enumerate(a):
    power = 0
    while val > 0:
        if val % 2 == 1:
            count[power].append(i)
        power +=1
        val = val >> 1

for power, val in list(count.items()):
    if len(val) >= 3:
        print(3)
        return

G = defaultdict(list)
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] & a[j] > 0:
            G[i].append(j) 
            G[j].append(i) 

min_cycle = n + 1
for key, _ in list(G.items()):
    qu = deque()
    qu.append((key, 0, None))
    visited = {}
    while len(qu) > 0:
        node = qu.popleft()
        visited[node[0]] = node[1]
        for child in G[node[0]]:
            if child not in visited:
                 qu.append((child, node[1] + 1, node[0]))
            else:
                if node[2] != child:
                    min_cycle = min(min_cycle, visited[child] + node[1] + 1)
if min_cycle == n + 1:
    print(-1)
else:
    print(min_cycle)


