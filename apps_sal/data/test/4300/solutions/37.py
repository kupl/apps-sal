n = int(input())
a = [int(x) for x in input().split()]
res = 0
for i in range(n):
  for j in range(i+1,n):
    res += a[i] * a[j]
print(res)
