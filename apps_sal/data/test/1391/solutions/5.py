def readn():
  return list(map(int, input().split()))
n,m,a=readn()#map(int,input().split())
b,p=sorted(map(int,input().split()))[-min(n,m):],sorted(map(int,input().split()))
r=min(n,m)
mm=r
l=0
while l<r:
    mid=(r+1 +l)//2
    pri=sum([max(0,p[i]-b[mm-mid+i]) for i in range(mid)])
    if pri<=a:
        l=mid
    else:
        r=mid-1
print(l,max(0,sum(p[:l])-a))






