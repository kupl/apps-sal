def q():
    n,m=map(int,input().split())
    p=[k for _ in range(n) for k in input()]
    w=[]
    for z in range(n):
        for j in range(m):
            ds=z*m+j
            w.append([])
            if j and p[ds]==p[ds-1]:
                w[-1].append(ds-1)
                w[-2].append(ds)
            if z and p[ds]==p[ds-m]:
                w[-1].append(ds-m)
                w[-1-m].append(ds)
    pol=[0]*len(p)
    def zss(g):
            pol[g]=1
            for f in w[g]:
                if not pol[f]:
                    w[f].remove(g)
                    zss(f)
                elif pol[f]==1:
                    raise OverflowError
            pol[g]=2
    for i,flag in enumerate(pol):
        if not flag:
            try:
                zss(i)
            except OverflowError:
                print('Yes')
                return
    print('No')
if 1==1:
    import sys
    sys.setrecursionlimit(10000)
    q()
