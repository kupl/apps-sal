from collections import defaultdict
from collections import deque

s = input().strip()
n = len(s)
dist = [0] * (n)
visited = [False] * n
d = defaultdict(list)
for i in range(n):
    d[s[i]].append(i)
visited[0] = True
stk = deque()
stk.append(0)
while stk:
    node = stk.popleft()
    if node == n - 1:
        break
    for i in d[s[node]]:
        if not visited[i] and i != node:
            dist[i] = dist[node] + 1
            visited[i] = True
            stk.append(i)
    d[s[node]] = []
    if node > 0 and not visited[node - 1]:
        stk.append(node - 1)
        visited[node - 1] = True
        dist[node - 1] = dist[node] + 1
    if node < n - 1 and not visited[node + 1]:
        stk.append(node + 1)
        visited[node + 1] = True
        dist[node + 1] = dist[node] + 1
print(dist[-1])
