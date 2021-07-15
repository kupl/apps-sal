import sys
n=int(input())
l1=-1
l2=-1
r1=10000000000
r2=10000000000
l1i=set()
l2i=set()
r1i=set()
r2i=set()
otv=0
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    if x==l1:
        l1i.add(i)
    elif x>l1 and x<l2:
        l1=x
        l1i={i}
    elif x==l2:
        l2i.add(i)
    elif x>l2:
        l1=l2
        l2=x
        l1i=l2i
        l2i={i}
    if y==r2:
        r2i.add(i)
    elif y>r1 and y<r2:
        r2=y
        r2i={i}
    elif y==r1:
        r1i.add(i)
    elif y<r1:
        r2=r1
        r1=y
        r2i=r1i
        r1i={i}
a=[l2]*len(l2i)
b=[l1]*len(l1i)
a.extend(b)
b=[r1]*len(r1i)
c=[r2]*len(r2i)
b.extend(c)
if len(l2i & r1i)>0:
    if b[1]-a[1]>0:
        print(b[1]-a[1])
    else:
        print(0)
else:
    if max(b[0]-a[1],b[1]-a[0])>0:
        print(max(b[0]-a[1],b[1]-a[0]))
    else:
        print(0)        
