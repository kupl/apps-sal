n,a,b=map(int,input().split())

from decimal import Decimal as de
l=sorted(list(map(int,input().split())),reverse=1)
fact=[1]
for i in range(1,51):
    fact.append(fact[-1]*i)
from collections import Counter as co
if l[0]==l[a-1]:
    def comb(x,y):
        return fact[x]//(fact[y]*fact[x-y]) if x>=y>=0 else 0
    x=co(l)[l[0]]
    print(l[0])
    print(sum(comb(x,i)for i in range(a,b+1)));return
ave=de(str(sum(l[:a])))/a
print(ave)

y=co(l[:a])[l[a-1]]
x=co(l)[l[a-1]]
print(fact[x]//(fact[y]*fact[x-y]))
