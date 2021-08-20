from collections import deque
n = int(input())
adj = [[] for i in range(n + 1)]
for (i, x) in enumerate(input().split()):
    i += 2
    x = int(x)
    adj[i].append(x)
    adj[x].append(i)
parents = [0 for i in range(n + 1)]
parents[1] = -1
colors = [-1] + [int(x) for x in input().split()]
q = deque([1])
while len(q) > 0:
    node = q.popleft()
    for x in adj[node]:
        if parents[x] == 0:
            parents[x] = node
            q.append(x)
ans = 1
for i in range(2, n + 1):
    if colors[i] != colors[parents[i]]:
        ans += 1
print(ans)
