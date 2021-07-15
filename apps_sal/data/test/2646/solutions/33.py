from collections import deque

N, M = map(int, input().split())

dist = [-1] * (N+1)
dist[1] = 0
connection = [[] for _ in range(N+1)]
ans = [-1] * (N+1)

for quel in range(M):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

que = deque()
que.append(1)

while que:
    v = que.popleft()

    for i in connection[v]:
        if dist[i] != -1:continue

        dist[i] = dist[v] + 1
        que.append(i)
        ans[i] = v

#print(dist)
print('Yes')
for j in range(2, N+1):
    print(ans[j])
