a,b,c,k = list(map(int,input().split()))
ans = 0
for x, y in zip([a,b,c], [1,0,-1]):
  if k <= 0:
    break
  ans += min(x,k) * y
  k -= min(x,k)

print(ans)
