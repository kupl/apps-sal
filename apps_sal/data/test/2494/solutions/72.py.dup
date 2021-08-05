from collections import deque

K = int(input())

G = [((10 * i % K, 0), ((i + 1) % K, 1)) for i in range(K)]
s = 1

dist = [10**9] * K
S = deque([s])
T = deque()
dist[s] = 0

d = 0
while S:
    while S:
        v = S.popleft()
        for w, c in G[v]:
            if d + c < dist[w]:
                dist[w] = d + c
                if c:
                    T.append(w)
                else:
                    S.append(w)
    S, T = T, S
    d += 1

print(dist[0] + 1)
