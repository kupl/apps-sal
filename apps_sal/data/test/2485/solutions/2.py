h,w,m=map(int,input().split())
item=[list(map(int,input().split())) for i in range(m)]
row=[0]*h
col=[0]*w
for i in range(m):
    x,y=item[i]
    row[x-1]+=1
    col[y-1]+=1
mr,mc=max(row),max(col)
xr=set([i for i in range(h) if row[i]==mr])
xc=set([i for i in range(w) if col[i]==mc])
check=len(xr)*len(xc)
for i in range(m):
    r,c=item[i]
    if r-1 in xr and c-1 in xc:
        check-=1
print(mr+mc if check>0 else mr+mc-1)
