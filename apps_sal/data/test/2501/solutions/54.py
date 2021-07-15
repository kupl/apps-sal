n = int(input())
a = list(map(int,input().split()))
ans = 0
d = {}
for i in range(n):
  if d.get(i+a[i],0)==0:
    d[i+a[i]] = [0,0]
  if d.get(i-a[i],0)==0:
    d[i-a[i]] = [0,0]
  d[i+a[i]][0] += 1
  d[i-a[i]][1] += 1
for v in d.values():
  ans += v[0]*v[1]
print(ans)
