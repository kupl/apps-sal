# 頂点を3回ずつに持つ (x歩目の着地）
# 最短路

import sys
input = sys.stdin.readline
N,M = list(map(int,input().split()))
if M == 0:
  print((-1))
  return
edge = [[] for _ in range(N+1)]
for _ in range(M):
  u,v = list(map(int,input().split()))
  edge[u].append(v)
S,T = list(map(int,input().split()))

INF = 10 ** 9
dist = [[INF,INF,INF] for _ in range(N+1)]

d = 0
q = [S]
while q:
  d += 1
  r = d % 3
  qq = []
  for u in q:
    for v in edge[u]:
      if dist[v][r] == INF:
        dist[v][r] = d
        qq.append(v)
  q = qq

d = dist[T][0]
answer = -1 if d == INF else d // 3
print(answer)

