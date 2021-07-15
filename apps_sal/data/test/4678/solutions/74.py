n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(1,n):
  d = max(a[i-1]-a[i],0)
  ans += d
  a[i] += d
print(ans)

