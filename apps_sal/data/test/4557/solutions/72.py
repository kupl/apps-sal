a,b,c = [int(x) for x in input().split()]
res = "YES"
if a > c:
  res = "NO"
if a + b < c:
  res = "NO"
print(res)
