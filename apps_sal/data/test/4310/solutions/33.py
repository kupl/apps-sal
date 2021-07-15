a = list(map(int, input().split()))
ans = 0
a.sort()
for i in range(len(a)-1):
  ans += a[i+1] - a[i]
print(ans)
