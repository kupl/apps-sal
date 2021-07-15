N, M = map(int, input().split())
a = []
c = []
for i in range(N):
  x, y = map(int, input().split())
  a.append([x, y])
for i in range(M):
  x, y = map(int, input().split())
  c.append([x, y])

for i in a:
  tmp = 10**9
  for l in range(M):
    j = c[l]
    x = abs(i[0]-j[0]) + abs(i[1]-j[1])
    if tmp > x:
      tmp = x
      ans = l + 1
  print(ans)
