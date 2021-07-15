n,m=map(int,input().split())
a=input().split()
b=input().split()
for i in range(n):
    a[i]=int(a[i])
for i in range(m):
    b[i]=int(b[i])
a.sort()
b.sort()
c=[]
for i in range(n):
    if a[i] in b:
        c.append(a[i])
    else:
        c.append(min(a[i]*10+b[0],b[0]*10+a[i]))
for i in range(m):
    if b[i] in a:
        c.append(b[i])
    else:
        c.append(min(b[i]*10+a[0],a[0]*10+b[i]))
print(min(c))
