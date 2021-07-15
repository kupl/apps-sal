n = int(input())
vt, va = 1, 1
for i in range(n):
  t, a = list(map(int, input().split()))
  d = max((t + vt - 1) // t, (a + va - 1) // a)
  vt = d * t
  va = d * a
print((vt + va))

