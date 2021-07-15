n, m  = list(map(int, input().split()))
pos = []
check = []
for i in range(n):
  a, b  = list(map(int, input().split()))
  pos.append([a, b])

for i in range(m):
  c, d  = list(map(int, input().split()))
  check.append([c, d])

for i in range(n):
  ans = 0
  k = 10**9
  for j in range(m):
    t = abs(pos[i][0] - check[j][0]) + abs(pos[i][1] - check[j][1])
    if k > t:
      k = t
      ans = j + 1
  print(ans)

