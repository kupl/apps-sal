from collections import deque
n, m = map(int, input().split())
G = [[] for i in range(3 * n)]
for i in range(m):
    u, v = map(int, input().split())
    for j in range(3):
        G[u + n * j - 1].append(v + n * ((j + 1) % 3) - 1)
s, g = map(int, input().split())
s = s - 1
g = g - 1
D = deque([s])
V = [0] * 3 * n
V[s] = 1
DD = [0] * 3 * n
while len(D) > 0:
    x = D[0]
    D.popleft()
    for y in G[x]:
        if V[y] == 0:
            V[y] = 1
            D.append(y)
            DD[y] = DD[x] + 1
if DD[g] == 0:
    print(-1)
else:
    print(DD[g] // 3)
