n,m,c = map(int,input().split())
b = list(map(int,input().split()))
ans = 0
for i in range(n):
  a = list(map(int,input().split()))
  cnt = 0
  for j in range(m):
    cnt += a[j]*b[j]
  if cnt + c > 0:
    ans += 1
print(ans)
