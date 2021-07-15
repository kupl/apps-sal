N, u, v = map(int, input().split())
u -= 1
v -= 1
tonari = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  tonari[a].append(b)
  tonari[b].append(a)

d_from_u = [float('inf') for _ in range(N)]
d_from_v = [float('inf') for _ in range(N)]
d_from_u[u] = 0
d_from_v[v] = 0
#print(tonari)

now = [u]
d = 0
while now:
  d += 1
  nextvisit = []
  for n in now:
    for t in tonari[n]:
      if d_from_u[t] > d:
        d_from_u[t] = d
        nextvisit.append(t)
  now = nextvisit

now = [v]
d = 0
while now:
  d += 1
  nextvisit = []
  for n in now:
    for t in tonari[n]:
      if d_from_v[t] > d:
        d_from_v[t] = d
        nextvisit.append(t)
  now = nextvisit

#print(d_from_u)
#print(d_from_v)

distance = []
for U, V in zip(d_from_u, d_from_v):
  distance.append((U, V))

distance.sort(key = lambda x: x[1])

#print(distance)
ans = 0
while distance:
  d = distance.pop()
  if d[0] < d[1]:
    ans = d[1] - 1
    break
print(ans)
