n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1,n):
  ans += min(a[i] - a[i-1],t)
print(ans+t)
