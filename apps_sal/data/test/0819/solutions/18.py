n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
if k==1:
    print(min(a))
elif k==2:
    b=max(a[0],a[-1])
    c=min(a)
    z=min(a[a.index(min(a)):])
    print(max(b,c,z))
else:
    print(max(a))

