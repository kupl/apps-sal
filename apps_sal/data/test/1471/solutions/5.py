N = int(input())
e = [[] for _ in range(N)]
for _ in range(N-1):
  u,v,w = map(int, input().split())
  u -= 1
  v -= 1
  e[u].append((v,w))
  e[v].append((u,w))

res = [-1]*N
res[0] = 0
q = [0]
while len(q):
  v = q.pop()
  for u,w in e[v]:
    if res[u]>=0:
      continue
    res[u] = res[v]+w
    q.append(u)

for r in res:
  print(r%2)
