n = int(input())
v = list(map(int, input().split()))
v.sort()
c = v[0]
for i in range(1,n):
  c = (v[i]+c)/2
print(c)
