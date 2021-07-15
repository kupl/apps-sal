n=int(input())
ans=0
ok=1
ng=n+1
while abs(ok-ng)>1:
    #print(ok,ng)
    mid=(ng+ok)>>1
    if (n+1)>=((mid*(mid+1))>>1):
        ok=mid
    else:
        ng=mid
ans=n-ok+1
print(ans)
