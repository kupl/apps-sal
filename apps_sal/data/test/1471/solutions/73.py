from collections import deque
N = int(input())
#隣接リスト
g = [[] for i in range(N)]
for i in range(N-1):
  u,v,w = list(map(int,input().split()))
  g[u-1].append([v-1,w])
  g[v-1].append([u-1,w])
q = deque()
#通ったかどうか
check = [0] * N
check[0] = 1
q.append(0)
ans = [-1] * N
ans[0] = 0
while len(q) > 0:
  e = q.popleft()
  for i,j in g[e]:
    if check[i] == 1:
      continue
    ans[i] = (ans[e] + j) %2
    check[i] = 1
    q.append(i)
for i in range(N):
  print((ans[i]))

