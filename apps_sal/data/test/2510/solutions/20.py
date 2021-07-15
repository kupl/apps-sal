from collections import deque

n,m = list(map(int, input().split()))
G = [[] for _ in range(n)]

for i in range(m):
    a,b = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

que = deque()
dist = [-1]*n
ans = 0
for i in range(n):
    if dist[i]!=-1:
        continue
    dist[i]==0
    que.append(i)
    cnt = 0
    while len(que):
        v = que.popleft()
        vs = G[v]
        for nv in vs:
            if dist[nv]==-1:
                dist[nv] = dist[v]+1
                cnt += 1
                que.append(nv)
    ans = max(cnt, ans)
if m==0:
    print((1))
else:
    print(ans)

