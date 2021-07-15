from collections import defaultdict
import sys
sys.setrecursionlimit(200000)

n, m = list(map(int, input().split(' ')))
roads = defaultdict(list)
visited = [False for _ in range(n)]
ans = 0
for _ in range(m):
    k, v = list(map(int, input().split(' ')))
    roads[k-1].append(v-1)
    roads[v-1].append(k-1)

def search(i):
    if visited[i]:
        visited[i] = True
        return True
    visited[i] = True
    for j in roads[i]:
        roads[j].remove(i)
        if search(j):
            return True
    return False

for i in range(n):
    if visited[i]:
        continue
    if not search(i):
        ans += 1

print(ans)

