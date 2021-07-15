n = int(input())
a = [int(x) for x in input().split()]
 
res = 0
for i in range(n):
  if a[i] == i+1:
    res += 1
    if i + 1 < n:
      a[i+1] = 0

print(res)
