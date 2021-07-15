a,b,n=[int(x) for x in input().split()]
ltm=[[]]*n
for i in range(n):
    ltm[i]=[int(x) for x in input().split()]
for i in range(n):
    l,t,m=ltm[i]
    maxr=(t-a)//b+1
    minr=l
    while maxr>=minr:
        r=(maxr+minr)//2
        if t*m>=(r-l+1)*(2*a+b*(r+l-2))/2:
            minr=r+1
        else:
            maxr=r-1
    r=maxr
    if r<l:
        print(-1)
    else:
        print(r)
