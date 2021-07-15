n,m=map(int, input().split())
alist=[list(map(int, input().split())) for l in range(n)]
alist.sort(key=lambda x:x[0])
ans=0
cnt=m
for i in range(n):
  if alist[i][1]<cnt:
    ans+=alist[i][0]*alist[i][1]
    cnt-=alist[i][1]
  else:
    ans+=cnt*alist[i][0]
    break
print(ans)
