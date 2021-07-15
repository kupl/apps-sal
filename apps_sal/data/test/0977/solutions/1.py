n,p = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
ansls = []
mx = max(a)
for i in range(1,mx+1):
  anstmp = 1
  for j in range(n)[::-1]:
    if a[j]-j > i:
      anstmp = 0
    else:
      anstmp *= n-max(i,a[j])+i-(n-j-1)
      anstmp %= p
  if anstmp:
    ans += 1
    ansls.append(i)
print(ans)
print(*ansls)
