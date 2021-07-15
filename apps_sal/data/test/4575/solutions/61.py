n = int(input())
d,x = [int(t) for t in input().split()]
a = []
for i in range(n):
  a.append(int(input()))
res = 0
for i in range(n):
  c = a[i]
  res += 1
  while c < d:
    res += 1
    c += a[i]
res += x
print(res)
