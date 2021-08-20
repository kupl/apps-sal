from collections import deque
N = int(input())
A = [list(map(int, input().split())) for _ in range(N - 1)]
(Q, K) = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(Q)]
d = [[] for _ in range(N)]
for (a, b, c) in A:
    d[a - 1].append([b - 1, c])
    d[b - 1].append([a - 1, c])
c = [0] * N
f = [False] * N
f[K - 1] = True
q = deque([K - 1])
while q:
    now = q.popleft()
    for (nex, cost) in d[now]:
        if f[nex]:
            continue
        c[nex] = c[now] + cost
        f[nex] = True
        q.append(nex)
for (x, y) in X:
    print(c[x - 1] + c[y - 1])
