N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
from collections import defaultdict
d=defaultdict(int)
d2=defaultdict(int)
a0=0
b0=0
c0=0
from math import gcd
for a,b in AB:
    if a==b==0:
        c0+=1
    elif a==0:
        a0+=1
    elif b==0:
        b0+=1
    else:
        if a<0:
            a,b=-a,-b
        g=gcd(a,b)
        a,b=a//g,b//g
        if b>0:
            d[(a,b)]+=1
        else:
            d2[(-b,a)]+=1
m=10**9+7
a=1
for k,v in d.items():
    if k in d2:
        a=a*(pow(2,v,m)+pow(2,d2[k],m)-1)%m
    else:
        a=a*pow(2,v,m)%m
for k,v in d2.items():
    if k not in d:
        a=a*pow(2,v,m)%m
print((a*(pow(2,a0,m)+pow(2,b0,m)-1)-1+c0)%m)
