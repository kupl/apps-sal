n=int(input())
a=int(input())
b=int(input())
if a!=b:
    m=[[a],[b]]
    while len(m[0])<6:
        p=m.pop(0)
        m.append(p+[a])
        m.append(p+[b])
    i=0
    while i < len(m):
        if m[i].count(b)!=2:
            m.pop(i)
        else:
            i+=1
else:
    m=[[a]*6]
d=6
for p in m:
    k=1
    x=n
    for t in p:
        x-=t
        if x<0:
            k+=1
            x=n-t
    d=min(d,k)
print(d)
