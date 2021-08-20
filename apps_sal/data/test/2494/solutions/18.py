from collections import deque
K = int(input())
G = [None] * K
for i in range(K):
    G[i] = ((10 * i % K, 0), ((i + 1) % K, 1))
s = 1
dist = [10 ** 9] * K
que = deque([s])
dist[s] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for (w, c) in G[v]:
        if d + c < dist[w]:
            dist[w] = d + c
            if c:
                que.append(w)
            else:
                que.appendleft(w)
print(dist[0] + 1)
