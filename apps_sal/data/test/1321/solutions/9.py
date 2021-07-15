n = int(input())
sum,h,w,c=0,[],[],[]
for i in range(n):
    a,b = map (int,input().split ())
    w.append(a)
    h.append(b)
    c.append(b)
    sum+=a
c.sort()
for i in range(n):
    mh = c[n-1]
    if (h[i] == mh):
        mh = c[n-2]
    print((sum-w[i])*mh,end=' ')
