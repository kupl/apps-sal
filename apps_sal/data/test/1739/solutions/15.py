n,x=list(map(int,input().split()))
l=list(map(int,input().split()))
from collections import Counter
l.sort()
gcd=sum(l[:n-1])
m=10**9+7
s=sum(l)
l1=[]
for i in l:
    l1.append(s-i-gcd)
c=Counter(l1)
l2=[]
for i in c:
    l2.append(i)
l2.sort()
z=True
while z:
    z=False
    for i in c.copy():
        a=c[i]
        b=0
        while a%x==0 and a!=0:
            z=True
            a//=x
            b+=1
        if z:
            c[i+b]+=a
            c[i]=0
y=l[-1]
for i in c:
    if c[i]:
        y=min(y,i)
gcd+=y
print(pow(x,min(s,gcd),m))

    
        

