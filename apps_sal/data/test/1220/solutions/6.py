N,M = map(int,input().split())

nE = [{i} for i in range(N)]
for _ in range(M):
  u,v = map(int,input().split())
  u,v = u-1,v-1
  nE[u].add(v)
  nE[v].add(u)

unvisited = set(range(N))
res = []

while unvisited:
  t = len(unvisited)
  s = next(iter(unvisited))
  unvisited.discard(s)
  stack = [s]
  while stack:
    v = stack.pop()
    s = unvisited & nE[v]
    stack.extend(unvisited-s)
    unvisited = s

  res.append(t-len(unvisited))

res.sort()
print(len(res))
print(' '.join(map(str,res)))
