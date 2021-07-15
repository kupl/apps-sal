n,x = map(int,input().split())
l = list(map(int,input().split()))
ans = 1
d = [0]*(n+1)
for i in range(1,n+1):
  d[i] = d[i-1]+l[i-1]
  if d[i] <= x:
    ans += 1
print(ans)
