import collections
import math

n=int(input())
a=list(map(int,input().split()))
ev=[a[2*i] for i in range(n//2)]
od=[a[2*i+1] for i in range(n//2)]

ccev=collections.Counter(ev)
ccod=collections.Counter(od)

mcev=ccev.most_common()
mcod=ccod.most_common()

if mcev[0][0]!=mcod[0][0]:
    print((n-mcev[0][1]-mcod[0][1]))
    return
elif len(mcev)==1 and len(mcod)==1:
    print((n-mcev[0][1]))
    return
elif len(mcev)==1:
    print((n-mcod[1][1]))
    return
elif len(mcod)==1:
    print((n-mcev[1][1]))
    return
else:
    tt=max(mcev[1][1],mcod[1][1])
    print((n-mcev[0][1]-tt))
    return

