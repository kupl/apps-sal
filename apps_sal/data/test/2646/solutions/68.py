from collections import deque

N, M = map(int, input().split())
dist = [-1] * N
# 初期化を忘れないように！スタート位置に既訪問フラグを立てる。ループ内では立てないので
dist[0] = 0
prv = [0] * N
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

d = deque()
d.append(0)

while d:
    now = d.popleft()
    for nv in G[now]:
        if dist[nv] == -1:
            # dist[nv]: 最短経路の長さを保持。この問題では不要なのでフラグとして１を入れるだけでも事足りる。
            dist[nv] = dist[now] + 1
            prv[nv] = now
            d.append(nv)

print("Yes")
for p in prv[1:]:
    print(p + 1)
