def read():
    return list(map(int,input().split()))
l,r,a=read()
if r<l:
    l,r=r,l
if l+a<r:
    print((l+a)*2)
else:
    a-=r-l
    print((r+a//2)*2)


