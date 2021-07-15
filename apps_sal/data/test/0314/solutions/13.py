q,w=list(map(int,input().split()))
a=list(map(int,input().split()))
if (w>8*q)|(w>sum(a)):
    print(-1)
else:
    s=0
    i=0
    while (w>0)&(i<q):
        s+=a[i]
        w-=min(8,s)
        s-=min(8,s)
        i+=1
    if w<=0:
        print(i)
    else:
        print(-1)

