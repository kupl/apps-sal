L, R = [int(i) for i in input().split()]

c = set()

for i in range(L, R + 1):
  t = i % 2019
  if t in c:
    break
  c.add(t)


m = float('inf')
l = list(c)
for i in range(len(l)):
  for j in range(i + 1, len(l)):
    m = min(m, l[i] * l[j] % 2019)

print(m)

