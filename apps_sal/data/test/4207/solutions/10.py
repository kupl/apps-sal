from collections import defaultdict
from math import gcd
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=defaultdict(int)
an=0
for i in range(n):
    if a[i]==0 and b[i]==0:an+=1
    elif a[i]!=0:
        x,y=(-b[i]//gcd(-b[i],a[i]),a[i]//gcd(-b[i],a[i]))
        if x<0:
            x*=-1;y*=-1
        if x==0:
            y=0

        l[(x,y)]+=1
#print(l)
print((sorted(l.values())[-1] if len(l)>0 else 0)+an)

