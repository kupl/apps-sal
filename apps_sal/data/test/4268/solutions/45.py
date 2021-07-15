n, d = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
t = 0
for i in range(n):
  for j in range(i+1, n):
    s = 0
    for b, c in zip(a[i], a[j]):
      s += (b - c) ** 2
    if s ** 0.5 == int(s ** 0.5):
      t += 1
print(t)
