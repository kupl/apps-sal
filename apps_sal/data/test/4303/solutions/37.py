n,k = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")
for i in range(n-k+1):
  l = abs(x[i]) + abs(x[i]-x[i+k-1])
  r = abs(x[n-1-i]) + (x[n-1-i]-x[n-k-i])
  ans = min(ans,l,r)
print(ans)
