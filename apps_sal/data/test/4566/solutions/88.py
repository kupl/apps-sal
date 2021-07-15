N, M = map(int, input().split())
L = []
for i in range(M):
  a, b = map(int, input().split())
  L.append(a)
  L.append(b)

for n in range(1, N+1):
  print(L.count(n))
