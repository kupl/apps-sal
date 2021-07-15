n,p,l,r = list(map(int,input().split()))
if l>1 and r<n:
    t1 = abs(p-l)+(r-l)
    t2 = abs(p-r)+(r-l)
    print(min(t1,t2)+2)
elif l>1 and r == n:
    print(abs(p-l)+1)
elif l==1 and r < n:
    print(abs(p-r)+1)
else:print(0)

