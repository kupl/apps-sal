from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
  u, v, w = map(int, input().split())
  g[u-1].append((v-1,w))
  g[v-1].append((u-1,w))
ds = [-1]*n
dq = deque([0])
ds[0] = 0
while dq:
  t = dq.popleft()
  for i in g[t]:
    if ds[i[0]] == -1:
      ds[i[0]] = ds[t] + i[1]
      dq.append((i[0]))
for i in ds:
  if i%2 == 0:
    print(0)
  else:
    print(1)
