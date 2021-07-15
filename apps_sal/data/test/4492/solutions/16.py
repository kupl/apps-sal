N, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(N-1):
  n = a[i]+a[i+1]
  if n > x:
    ans += n-x
    if n-x > a[i+1]:
      a[i], a[i+1] = a[i]-(n-x-a[i+1]), 0
    else:
      a[i+1] -= (n-x)
print(ans)
