n = int(input())
d = 1
for i in range(1,n+1):
  d = (d*i)%(10**9+7)
print(d)
