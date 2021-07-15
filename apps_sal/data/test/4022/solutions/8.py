n=int(input())
o=[]
c=[]
l3=[]
for i in range(n):
    r,s=map(int,input().strip().split())
    l3.append([r,s])
    o.append(r)
    c.append(s)
o.sort()
c.sort()
e1=o[-1]
e2=c[0]
if (e1<=e2):
    ans=e2-e1
else:
    ans=0
for i in l3:
    a1=i[0]
    a2=i[1]
    if a1==e1:
        w1=o[-2]
    else:
        w1=e1
    if a2==e2:
        w2=c[1]
    else:
        w2=e2
    ans=max(w2-w1,ans)
print (ans)
