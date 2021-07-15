n , m = map(int, input().split())
e = 0
d = []
for i in range(1, n + 1):
  l = list(map(int, input().split()))
  for a in range(l[0]):
    b = l[a + 1]
    d.append(b)
for j in range(1, m + 1):
  c = 0
  for k in d:
    if k == j:
      c += 1
  if c == n:
    e += 1
print(e)
