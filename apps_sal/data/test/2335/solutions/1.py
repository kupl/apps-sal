n=int(input())
g=[]
r=[]
b=[]
lr=0
lb=0
lg=0
for i in range(n):
    a=input().split(" ")
    if a[1]=="G":
        g.append(int(a[0]))
        lg+=1
    if a[1]=="R":
        r.append(int(a[0]))
        lr+=1
    if a[1]=="B":
        b.append(int(a[0]))
        lb+=1
g=g[::-1]
r=r[::-1]
b=b[::-1]
s=0
if lg>0:
    for i in range(lg+1):
        if i==0:
            ps=0
            if lr>0:
                if r[lr-1]<g[lg-1]:
                    ps+=g[lg-1]-r[lr-1]
                    while r[lr-1]<g[lg-1]:
                        lr-=1
                        if lr==0:
                            break
            if lb>0:
                if b[lb-1]<g[lg-1]:
                    ps+=g[lg-1]-b[lb-1]
                    while b[lb-1]<g[lg-1]:
                        lb-=1
                        if lb==0:
                            break
            s+=ps
        elif i==lg:
            ps=0
            if lr>0:
                ps+=r[0]-g[0]
            if lb>0:
                ps+=b[0]-g[0]
            s+=ps
        else:
            ps=0
            d=g[lg-i-1]-g[lg-i]
            rin=False
            blin=False
            if lr>0:
                if r[lr-1]<g[lg-i-1]:
                    rin=True
                    mdr=r[lr-1]-g[lg-i]
                    if lr>1:
                        while r[lr-2]<g[lg-i-1]:
                            mdr=max(mdr,r[lr-2]-r[lr-1])
                            lr-=1
                            if lr==1:
                                break
                    mdr=max(mdr,g[lg-i-1]-r[lr-1])
                    lr-=1
            if lb>0:
                if b[lb-1]<g[lg-i-1]:
                    blin=True
                    mdb=b[lb-1]-g[lg-i]
                    if lb>1:
                        while b[lb-2]<g[lg-i-1]:
                            mdb=max(mdb,b[lb-2]-b[lb-1])
                            lb-=1
                            if lb==1:
                                break
                    mdb=max(mdb,g[lg-i-1]-b[lb-1])
                    lb-=1
            if blin and rin:
                ps+=min(2*d,3*d-mdr-mdb)
            else:
                ps+=d
                if blin:
                    ps+=d-mdb
                elif rin:
                    ps+=d-mdr
            s+=ps
else:
    if lr>0:
        s+=r[0]-r[-1]
    if lb>0:
        s+=b[0]-b[-1]
print(s)
