n=int(input())
l=list(map(float,input().split()))
l=sorted(l)
l=l[::-1]
ans=0
d=1
vze=0
for x in l :
    vze=vze+x*(d-vze)
    d*=(1-x)
    ans=max(ans,vze)
print(ans)
