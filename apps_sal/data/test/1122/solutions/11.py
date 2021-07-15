n,m = map(int,input().split())
l=1
if n%2==1:
    r=n
    for i in range(m):
        d=min(abs(l-r),n-abs(l-r))
        print(l,r)
        l+=1
        r-=1
else:
    if n%4==0:
        r=n-1
    else:
        r=n
    rev=False
    for i in range(m):
        d=min(abs(l-r),n-abs(l-r))
        if d == n//2:
            rev=True
            l+=1
            print(l,r)
        else:
            print(l,r)
        l+=1
        r-=1
