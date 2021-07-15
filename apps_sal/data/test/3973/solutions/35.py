
def main(n,m,a):
    mat=[0]*m
    dat=[set() for _ in range(m)]
    ret=[0]*m
    base=0
    for i in range(n-1):
        base+=(a[i+1]-a[i])%m
        if (a[i+1]-a[i])%m<2:continue
        mat[a[i+1]-1]+=(a[i+1]-a[i])%m-1
        dat[a[i+1]-1].add(i+1)
        dat[(a[i])%m].add(-i-1)
    now=0
    nowd=set()
    for i in range(m-1,-1,-1):
        now+=mat[i]
        mat[i]=0
        ret[i]+=now
        delid=set()
        for x in dat[i]:
            if x>0:
                nowd.add(x)
                delid.add(x)
            elif -x in nowd:
                nowd.discard(-x)
                delid.add(x)
        for x in delid:
            dat[i].discard(x)
        now=max(now-len(nowd),0)
    for i in range(m-1,-1,-1):
        now+=mat[i]
        mat[i]=0
        ret[i]+=now
        delid=set()
        for x in dat[i]:
            if x>0:
                nowd.add(x)
                delid.add(x)
            elif -x in nowd:
                nowd.discard(-x)
                delid.add(x)
        for x in delid:
            dat[i].discard(x)
        now=max(now-len(nowd),0)
    
    return base-max(ret)
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
print((main(n,m,a)))

