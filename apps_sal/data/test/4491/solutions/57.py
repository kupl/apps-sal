n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
res = 0
for i in range(n):
  c = 0
  for j in range(n):
    if j < i:
      c += a[j]
    elif j == i:
      c += a[j]
      c += b[j]
    else:
      c += b[j]
  res = max(res,c)
print(res)
