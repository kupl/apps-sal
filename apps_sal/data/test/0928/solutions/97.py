n,k = map(int,input().split())
a = list(map(int,input().split()))
r,cnt,tmp = 0,0,0
for l in range(n):
  while r<n and tmp+a[r]<k:
    tmp += a[r]
    r += 1
  cnt += n-r
  if l==r:
    r += 1
  else:
    tmp -= a[l]
print(cnt)
