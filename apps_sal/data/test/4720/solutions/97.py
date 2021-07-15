n = int(input())
res = 0
for i in range(n):
  a = [int(x) for x in input().split()]
  res += a[1] - a[0] + 1
print(res)
