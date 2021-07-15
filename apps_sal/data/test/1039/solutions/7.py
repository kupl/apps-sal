N = int(input())
G = [[] for n in range(N)]

for n in range(N-1):
  a,b,c = map(int,input().split())
  G[a-1].append((b-1,c))
  G[b-1].append((a-1,c))

Q,K = map(int,input().split())
d = N*[-1]
d[K-1] = 0
q = [K-1]

while q:
  t = q.pop()
  for b,c in G[t]:
    if d[b]==-1:
      d[b] = d[t]+c
      q.append(b)

for q in range(Q):
  x,y = map(int,input().split())
  print(d[x-1]+d[y-1])
