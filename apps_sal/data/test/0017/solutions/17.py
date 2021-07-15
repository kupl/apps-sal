n,k,t = map(int,input().split())
if t <= k:
  res = t
elif t <= n:
  res = k
else:
  res = (n+k) - t
print(res)
