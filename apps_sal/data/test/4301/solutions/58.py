n = int(input())
a = [int(input()) for _ in range(n)]
m1, m2 = -1, -1
for i in range(n):
  if m1 < a[i]:
    m2 = m1
    m1 = a[i]
  elif m2 < a[i]:
    m2 = a[i]
for i in range(n):
  if a[i] == m1:
    print(m2)
  else:
    print(m1)

