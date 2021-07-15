n, k = map(int, input().split())

ans = 0
if k == 0:
  print (n**2)
  return
for i in range(1,n+1):
  if i <= k:
    continue
  ans += max(i-k,0)*(n//i) + max(n%i-(k-1),0)
print (ans)
