import collections
n=int(input())
a=list(map(int,input().split()))
c = collections.Counter(a)
b=[0,0]
d=[0,0]
for i in c:
    if c[i]>=4:
        b.append(i)
    elif c[i]>=2:
        d.append(i)
b.sort(reverse=True)
d.sort(reverse=True)
if b[0]>d[0]:
    print((b[0]*b[0]))
elif b[0]<d[1]:
    print((d[0]*d[1]))
else:
    print((b[0]*d[0]))

