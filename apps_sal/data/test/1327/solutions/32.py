n,m = map(int, input().split(" "))
a = [list(map(int, input().split(" "))) for i in range(n)]
ans = 0
#print(a)
for i in range(2 ** 3):
  total = []
  minus = [1 for _ in range(3)]
  for j in range(3):
    if i >> j & 1:
      minus[j] *= -1
  for k in range(n):
    total.append(a[k][0] * minus[0] + a[k][1] * minus[1] + a[k][2] * minus[2])
  ans = max(ans, sum(sorted(total, reverse=1)[:m]))
print(ans)
