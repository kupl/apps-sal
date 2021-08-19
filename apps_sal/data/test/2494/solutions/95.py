from collections import deque
K = int(input())
G = [[] for i in range(K)]
for i in range(K):
    G[i].append(((i + 1) % K, 1))
    G[i].append((10 * i % K, 0))
dist = [float('inf')] * K
dist[1] = 1
que = deque()
que.append(1)
while que:
    n = que.pop()
    for (v, c) in G[n]:
        if dist[v] > dist[n] + c:
            dist[v] = dist[n] + c
            if c == 0:
                que.append(v)
            else:
                que.appendleft(v)
print(dist[0])
