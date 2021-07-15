n, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))[::-1]
m = n
for j in range(len(a)):
  waste = min(a[j] // 4, m)
  m -= waste
  a[j] -= waste * 4
  if m == 0:
    break
m1, m2, m3, msukabljat = 0, 0, 0, []
for x in a:
  m1 += (x == 1)
  m2 += (x == 2)
  m3 += (x == 3)
  msukabljat += ([x] if x >= 4 else [])
waste = min(m1, m2, m)
m, m1, m2 = m - waste, m1 - waste, m2 - waste
waste = min(m3 // 2, m // 2)
m, m3 = m - waste * 2, m3 - waste * 2
waste = min(m2 // 3, m // 2)
m, m2 = m - waste * 2, m2 - waste * 3
waste = min(m1, m2, m3, m // 2)
m, m1, m2, m3 = m - waste * 2, m1 - waste, m2 - waste, m3 - waste
waste = min(m3, m)
m, m3 = m - waste, m3 - waste
waste = min(m1 // 2, m)
m, m1 = m - waste, m1 - 2 * waste
waste = min(m1, m)
m, m1 = m - waste, m1 - waste
waste = min(m2, m)
m, m2 = m - waste, m2 - waste
if m1 + m2 + m3 * 2 + sum([x // 2 + x % 2 for x in msukabljat]) <= 2 * n:
  print("YES")
else:
  print("NO")


