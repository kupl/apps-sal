from collections import deque
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
deg = [0 for i in range(N)]
for i in range(N):
    for p in G[i]:
        deg[p] += 1
q = deque(i for i in range(N) if deg[i] == 0)
res = []
while q:
    u = q.popleft()
    res.append(u)
    for v in G[u]:
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)
if len(res) == N:
    print(-1)
    return
X = {i for i in range(N)}
for st in range(N):
    pre = [-1 for i in range(N)]
    q = deque([st])
    flag = 0
    while(q):
        r = q.popleft()
        for p in G[r]:
            if pre[p] == -1:
                pre[p] = r
                q.append(p)
            if pre[st] != -1:
                Y = {st}
                tmp = pre[st]
                while(tmp != st):
                    Y.add(tmp)
                    tmp = pre[tmp]
                if len(Y) < len(X):
                    X = {i for i in Y}
                flag = 1
                break
        if flag:
            break
print(len(X))
for i in X:
    print(i + 1)
