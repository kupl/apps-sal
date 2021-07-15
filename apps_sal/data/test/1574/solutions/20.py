(n,m) = (int(i) for i in input().split())
c={}

b=[0]*(n+1)
q=10000000
for j in range(m):
    (a,g) = (int(i) for i in input().split())
    if(a in list(c.keys())):
        c[a].append(g)
    else:
        c[a]=[g]
    if(g in list(c.keys())):
        c[g].append(a)
    else:
        c[g]=[a]
    b[a]=b[a]+1
    b[g]=b[g]+1

for first in list(c.keys()):
    for second in c[first]:
        if(first>second):
            for third in c[second]:
                if(third in c[first])and(third!=first)and(second>third):
                    if(q>b[third]+b[second]+b[first]-6):
                        q=b[third]+b[second]+b[first]-6


if(q==10000000):
    print(-1)
else:
    print(q)

